import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def recognize_and_translate(input_lang='en', output_lang='hi'):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            # Recognize speech
            text = recognizer.recognize_google(audio, language=input_lang)
            print("Recognized:", text)
    except Exception as e:
        print("Speech recognition error:", e)
        return None, None

    try:
        translator = Translator()
        translated = translator.translate(text, src=input_lang, dest=output_lang).text
        tts = gTTS(translated, lang=output_lang)
        output_file = "translated_audio.mp3"
        tts.save(output_file)
        return translated, output_file
    except Exception as e:
        print("Translation/TTS error:", e)
        return None, None
