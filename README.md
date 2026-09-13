# Local Bilingual Speech-to-Text (Vosk)

This project is a 100% local, offline Speech-to-Text (STT) application written in Python. It uses the [Vosk](https://alphacephei.com/vosk/) library to transcribe audio from your microphone in real-time. It features voice-triggered language switching between Turkish and English, filtering out intermediate listening states to provide clean, final transcribed sentences.

## Features

* **100% Offline & Free:** No API keys, no internet connection required, and no usage limits.
* **Voice-Triggered Language Switching:** Seamlessly switch between Turkish and English models by saying specific trigger words (e.g., "İngilizce" or "Türkçe").
* **Clean Output:** Filters out intermediate listening states and only outputs the final transcribed sentences.
* **Lightweight:** Runs efficiently on standard CPUs without requiring high-end GPUs.

## Prerequisites

* **Python 3.7+**
* A working microphone.

## Installation

Follow these steps carefully to install the required libraries and set up the language models.

### Step 1: Install Required Python Packages

Open your terminal or command prompt and install the necessary libraries via `pip`:

```bash
pip install vosk sounddevice
```

### Step 2: Download the Language Models

The application requires pre-trained acoustic models to recognize speech. Download the "small" models for both Turkish and English from the official Vosk repository:

* **Turkish Model:** [vosk-model-small-tr-0.3.zip](https://alphacephei.com/vosk/models/vosk-model-small-tr-0.3.zip) (approx. 35 MB)
* **English (US) Model:** [vosk-model-small-en-us-0.15.zip](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip) (approx. 36 MB)

*(For a full list of available models, visit the [Vosk Models Page](https://alphacephei.com/vosk/models)).*

### Step 3: Set Up the Folder Structure

The application expects the models to be located in specific folders relative to your Python script. 

1. Create a main folder for your project.
2. Inside your project folder, create a new folder named exactly **`model`**.
3. Extract the downloaded Turkish zip file, rename the extracted folder to **`tr`**, and place it inside the `model` folder.
4. Extract the downloaded English zip file, rename the extracted folder to **`en`**, and place it inside the `model` folder.
5. Place your Python script (e.g., `app.py`) in the main project folder.

Your final directory structure **must** look exactly like this:

```text
your_project_folder/
│
├── app.py                  # Your main Python script
└── model/                  # The main model directory
    ├── en/                 # English model files
    │   ├── final.mdl
    │   ├── HCLr.fst
    │   └── ...
    └── tr/                 # Turkish model files
        ├── final.mdl
        ├── HCLr.fst
        └── ...
```

## Usage

Run the script from your terminal or IDE (like Thonny, VS Code, or PyCharm):

```bash
python app.py
```

### Voice Commands

The system starts in **Turkish** by default. Use the following voice commands to control the application:

* **Switch to English:** Say `"İngilizce"`, `"İngilizceye"`, or `"English"` while in Turkish mode.
* **Switch to Turkish:** Say `"Türkçe"`, `"Türkçeye"`, or `"Turkish"` while in English mode.
* **Exit Application:** Say `"Kendini kapat"` or `"Kill the program"` to safely terminate the script.

### Example Output

```text
--------------------------------------------------
SİSTEM HAZIR! Şu anki aktif dil: TÜRKÇE
- İngilizceye geçmek için: 'İngilizce' deyin.
- Türkçeye dönmek için: 'Türkçe' deyin.
--------------------------------------------------
[TR] test deneme bir iki
[TR] i̇ngilizceye geç
---> DİL DEĞİŞTİRİLDİ: İNGİLİZCE (You can start speaking English)
[EN] hello how are you today
[EN] kill the program
SİSTEM KAPATILIYOR... / SHUTTING DOWN...
```
