import sys
import speech_recognition as sr

# Get the language choice from command line arguments
if len(sys.argv) < 2:
    print("Usage: python stt.py 1 for ENG 2 for TR")
    exit()
elif sys.argv[1] == "1":
    language = "en-US"
elif sys.argv[1] == "2":
    language = "tr-TR"
else:
    print("Invalid language choice. Please choose 1 or 2. // 1 for ENG 2 for TR")
    exit()

# Initialize the recognizer
r = sr.Recognizer()

while True:
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        try:
            # Listen for audio and store it in audio_data
            audio_data = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("Timed out waiting for speech. Starting again...")
            continue

    # Convert speech to text
    try:
        text = r.recognize_google(audio_data, language=language)
    except sr.UnknownValueError:
        print("Could not understand speech.")
        continue
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        continue

    # Print the text
    print(text)
    
    if text.lower() == "kill the program":
        print("I AM GOING TO DIE...!!!!...")
        exit()
    elif text.lower() == "kendini kapat":
        print("HAYIRRRRRRRRRR...!!!...")
        exit()
    else:
        continue

