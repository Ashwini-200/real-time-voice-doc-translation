# real-time-voice-doc-translation
Real-time Voice and Document Translation project in Python. Converts spoken input into selected languages and translates text documents. Uses Google Speech Recognition, Google Translate API, and gTTS for voice output, enabling multilingual communication and learning.
Real-Time Voice and Document Translation

This project is a real-time voice and document translation application that can handle:

Real-time spoken audio – Translate while you speak.

Recorded audio files – Upload audio files for translation.

Document files – Upload text documents to translate their content.

Supports multiple Indian languages (Kannada, Tamil, Telugu, Hindi) and English.

Features

Record live audio and translate instantly.

Upload recorded audio files for translation.

Upload text documents (PDF, TXT, DOCX) and translate their content.

Detect language automatically.

Convert translated text into speech using gTTS.

Simple interactive interface with Streamlit.
Installation

Clone the repository
git clone <repository-url>
cd <repository-folder>

Create a virtual environment
python -m venv venv

Activate the virtual environment

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install dependencies
python -m pip install --upgrade pip
python -m pip install langdetect
pip install -r requirements.txt

Usage

Run the application using Streamlit:
streamlit run app.py

Once the app opens in your browser, you can:

Speak in real-time – Translate and listen to your speech.

Upload an audio file – Get translation and speech output.

Upload a document – Translate its text and listen to the result.

Code Overview

app.py – Main Streamlit application. Handles UI, input selection, audio recording, document parsing, translation, and speech output.

requirements.txt – Contains all Python libraries required for the project.

langdetect – Detects the language of the input automatically.

gTTS – Converts translated text into audio output.

Document processing modules – Extract text from PDFs, DOCX, and TXT files for translation.

Contribution

Contributions and improvements are welcome! Open issues or pull requests for new features.

License

This project is licensed under the MIT License.
