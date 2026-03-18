import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile
import docx2txt
import PyPDF2

from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # ensures consistent detection results

st.set_page_config(page_title="Real-Time Voice Translator", layout="centered")
st.title("🗣️ Real-Time Voice & File Translator")

translator = Translator()

LANGUAGES = {
    'English': 'en',
    'Hindi': 'hi',
    'Kannada': 'kn',
    'Telugu': 'te',
    'Tamil': 'ta'
}

input_lang = st.selectbox("🎙️ Select Input Language", list(LANGUAGES.keys()))
output_lang = st.selectbox("🗣️ Select Output Language", list(LANGUAGES.keys()))

option = st.radio("Choose input method:", ['🎤 Speak Now', '📁 Upload Audio File', '📄 Upload Text Document'])

class TranslationError(Exception):
    """Raised when detected input language doesn't match selected source."""
    pass

def detect_and_validate(text, selected_source_code):
    detected = detect(text)
    if detected != selected_source_code:
        raise TranslationError(
            f"Detected language '{detected}' does not match the selected source '{selected_source_code}'."
        )
    return detected

def translate_and_speak(text, target_lang_key):
    translation = translator.translate(text, dest=LANGUAGES[target_lang_key])
    st.success(f"📝 Translated Text: {translation.text}")
    tts = gTTS(translation.text, lang=LANGUAGES[target_lang_key])
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        st.audio(tmp.name, format="audio/mp3")
    os.remove(tmp.name)

# Handle Speech Input
if option == '🎤 Speak Now':
    if st.button("Start Recording"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎙️ Listening... Speak clearly.")
            audio = r.listen(source, phrase_time_limit=10)
        try:
            text = r.recognize_google(audio, language=LANGUAGES[input_lang])
            st.write(f"🔊 You said: {text}")
            try:
                detect_and_validate(text, LANGUAGES[input_lang])
                translate_and_speak(text, output_lang)
            except TranslationError as te:
                st.error(f"❌ {te}")
        except Exception as e:
            st.error(f"❌ Could not recognize speech: {e}")

# Handle Uploaded Audio File
elif option == '📁 Upload Audio File':
    AUDIO_EXTS = ['mp3', 'wav', 'm4a', 'aac', 'flac', 'ogg', 'opus']
    uploaded_audio = st.file_uploader("Upload Audio File", type=AUDIO_EXTS)

    def convert_to_pcm_wav(uploaded_file, ext):
        try:
            audio_file = AudioSegment.from_file(uploaded_file, format=ext)
            audio_file = audio_file.set_frame_rate(16000).set_channels(1).set_sample_width(2)
            temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            audio_file.export(temp_wav.name, format="wav")
            return temp_wav.name
        except Exception as e:
            st.error(f"❌ Could not convert audio: {e}")
            return None

    if uploaded_audio:
        ext = uploaded_audio.name.split('.')[-1].lower()
        st.info("🔄 Converting and transcribing audio...")
        wav_path = convert_to_pcm_wav(uploaded_audio, ext)

        if wav_path:
            r = sr.Recognizer()
            with sr.AudioFile(wav_path) as source:
                audio = r.record(source)
                try:
                    text = r.recognize_google(audio, language=LANGUAGES[input_lang])
                    st.write(f"🔊 Transcribed Text: {text}")
                    try:
                        detect_and_validate(text, LANGUAGES[input_lang])
                        translate_and_speak(text, output_lang)
                    except TranslationError as te:
                        st.error(f"❌ {te}")
                except Exception as e:
                    st.error(f"❌ Error transcribing audio: {e}")
            os.remove(wav_path)

# Handle Document Upload
elif option == '📄 Upload Text Document':
    uploaded_doc = st.file_uploader("Upload Document (TXT, PDF, DOCX)", type=['txt', 'pdf', 'docx'])
    if uploaded_doc:
        ext = uploaded_doc.name.split('.')[-1].lower()
        text = ""
        if ext == 'txt':
            text = uploaded_doc.read().decode('utf-8')
        elif ext == 'docx':
            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
                tmp.write(uploaded_doc.read())
                tmp_path = tmp.name
            text = docx2txt.process(tmp_path)
            os.remove(tmp_path)
        elif ext == 'pdf':
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_doc.read())
                tmp_path = tmp.name
            with open(tmp_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = "\n".join([page.extract_text() for page in reader.pages])
            os.remove(tmp_path)

        if text.strip():
            st.write("📝 Extracted Text:")
            st.text_area("Document Text", value=text, height=150)
            try:
                detect_and_validate(text, LANGUAGES[input_lang])
                translate_and_speak(text, output_lang)
            except TranslationError as te:
                st.error(f"❌ {te}")
        else:
            st.warning("❗ Could not extract text from the document.")
