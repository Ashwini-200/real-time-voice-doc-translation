# real-time-voice-doc-translation
Real-time Voice and Document Translation project in Python. Converts spoken input into selected languages and translates text documents. Uses Google Speech Recognition, Google Translate API, and gTTS for voice output, enabling multilingual communication and learning.
Real-Time Voice and Document Translation

# Real-Time Voice and Document Translation

This project is a **real-time voice and document translation application** that supports:

- 🎤 Real-time speech translation  
- 🔊 Recorded audio file translation  
- 📄 Document translation (PDF, DOCX, TXT)  

It supports multiple languages including **Kannada, Tamil, Telugu, Hindi, and English**.

---

## Features

- Real-time voice input and translation  
- Upload and translate recorded audio files  
- Upload and translate documents (PDF, DOCX, TXT)  
- Automatic language detection using `langdetect`  
- Text-to-speech output using `gTTS`  
- Simple UI using Streamlit  

---

## Project Structure
real_time_voice_translator/
│
├── app.py # Main Streamlit app
├── voice_engine.py # Audio + document processing + translation logic
├── requirements.txt # Dependencies
├── README.md

---

## Installation & Execution (Windows CMD)

Run the following commands step-by-step:
python -m venv venv
venv\Scripts\activate

python -m pip install langdetect


pip install -r requirements.txt


streamlit run app.py


---

## Requirements

Make sure your `requirements.txt` contains:


streamlit>=1.20.0
gTTS>=2.2.3
googletrans==4.0.0-rc1
speechrecognition>=3.8.1
pyaudio>=0.2.11
langdetect>=1.0.9


---

## Additional Setup

### FFmpeg (Required for Audio Processing)

Install FFmpeg and add it to system PATH.

Check installation:

---

## Usage

After running:

Open browser:

- Local URL: http://localhost:8503  

---

## How It Works

1. User selects input type:
   - Real-time voice  
   - Audio file  
   - Document  

2. Input is processed in `voice_engine.py`:
   - Audio → Speech Recognition  
   - Document → Text Extraction  

3. Language is detected using `langdetect`  

4. Text is translated using `googletrans`  

5. Output is converted to speech using `gTTS`  

---

## Contribution

Feel free to contribute by:
- Adding more languages  
- Improving UI  
- Enhancing translation accuracy  

---

## License

This project is licensed under the MIT License.
