# Local Bilingual Speech-to-Text (Vosk)

This project is a 100% local, offline Speech-to-Text (STT) application written in Python. It uses the [Vosk](https://alphacephei.com/vosk/) library to transcribe audio from your microphone in real-time. It features voice-triggered language switching between Turkish and English, filtering out intermediate listening states to provide clean, final transcribed sentences.

## Features

* **100% Offline & Free:** No API keys, no internet connection required, and no usage limits.
* **Voice-Triggered Language Switching:** Seamlessly switch between Turkish and English models by saying specific trigger words.
* **Clean Output:** Filters out intermediate listening states and only outputs the final transcribed sentences.
* **Hardware Scalable:** Can run on low-end hardware (Raspberry Pi) using lightweight models, or scale up to utilize modern 12-core CPUs and 16GB RAM setups with massive, high-accuracy models.

## Prerequisites

* **Python 3.7+**
* A working microphone.
* `pip install vosk sounddevice`

---

## Model Selection & Download Links

Depending on your hardware (CPU cores and RAM) and your specific use case, you can choose different English models. The application folder structure remains the same regardless of which model you choose—simply extract the contents into the `model/en/` directory.

### 🇹🇷 Turkish Model
*   **[vosk-model-small-tr-0.3 (35 MB)](https://alphacephei.com/vosk/models/vosk-model-small-tr-0.3.zip)**
    *   The standard, lightweight model for Turkish. Highly responsive and efficient.

### 🇺🇸 English Models (Choose One)
*   **Option 1: Lightweight / Fast**
    *   **[vosk-model-small-en-us-0.15 (40 MB)](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip)**
    *   *Best for:* Older hardware, Raspberry Pi, or situations where memory is heavily constrained.
    *   *Trade-off:* Higher Word Error Rate (WER ~9.85%).
*   **Option 2: High Accuracy / Generic Use**
    *   **[vosk-model-en-us-0.22 (1.8 GB)](https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip)**
    *   *Best for:* General dictation, short commands, and everyday use on modern PCs (e.g., 16GB RAM, multi-core CPU).
    *   *Trade-off:* Requires more RAM. Halves the error rate compared to the small model (WER ~5.69%).
*   **Option 3: Continuous & Long-Form Speech**
    *   **[vosk-model-en-us-0.42-gigaspeech (2.3 GB)](https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip)**
    *   *Best for:* Podcasts, storytelling, long paragraphs, and continuous dictation. It understands context and transitions much better.
    *   *Hardware Note:* Easily handled by 16GB RAM systems (consumes ~2.5 - 3GB when running). Requires a strong CPU (like an Intel Core Ultra 5 12-core) for real-time processing.

---

## Installation & Setup

1. Create a main folder for your project.
2. Inside your project folder, create a new folder named exactly **`model`**.
3. Download the Turkish model and extract it. Rename the extracted folder to **`tr`** and place it inside the `model` folder.
4. Download your preferred English model and extract it. Rename the extracted folder to **`en`** and place it inside the `model` folder.
5. Place your Python script (`app.py`) in the main project folder.

Your final directory structure **must** look exactly like this:

```text
your_project_folder/
│
├── app.py                  # Your main Python script
└── model/                  # The main model directory
    ├── en/                 # English model files (40MB, 1.8GB, or 2.3GB)
    │   ├── final.mdl
    │   ├── HCLr.fst
    │   └── ...
    └── tr/                 # Turkish model files
        ├── final.mdl
        ├── HCLr.fst
        └── ...
