import vosk
import sys
import sounddevice as sd
import queue
import json
import re

# Model yolları (Klasör yapınızın model/tr ve model/en olduğuna emin olun)
MODEL_TR_PATH = "model/tr"
MODEL_EN_PATH = "model/en"
SAMPLE_RATE = 16000

q = queue.Queue()

def callback(indata, frames, time, status):
    # status uyarısını da gizliyoruz ki ekranda gereksiz yazılar çıkmasın
    if status:
        pass
    q.put(bytes(indata))

def clean_text(text):
    text = text.lower()
    text = text.replace('i̇', 'i').replace('ı', 'i')
    text = re.sub(r'[^a-z\s]', '', text)
    return text.strip()

TRIGGERS_TO_EN = ["ingilizce", "english", "ingiliz", "ingilizceye"]
TRIGGERS_TO_TR = ["turkce", "turkish", "turk", "turkceye"]

print("--------------------------------------------------")
print("Modeller belleğe yükleniyor (Bu işlem 10-15 saniye sürebilir)...")
try:
    model_tr = vosk.Model(MODEL_TR_PATH)
    model_en = vosk.Model(MODEL_EN_PATH)
except Exception as e:
    print(f"HATA: Modeller yüklenemedi. Lütfen 'model/tr' ve 'model/en' yollarını kontrol edin.\nDetay: {e}")
    sys.exit(1)

rec_tr = vosk.KaldiRecognizer(model_tr, SAMPLE_RATE)
rec_en = vosk.KaldiRecognizer(model_en, SAMPLE_RATE)

active_rec = rec_tr
current_lang = "TR"

print("--------------------------------------------------")
print("SİSTEM HAZIR! Şu anki aktif dil: TÜRKÇE")
print("- İngilizceye geçmek için: 'İngilizce' veya 'English' deyin.")
print("- Türkçeye dönmek için: 'Türkçe' veya 'Turkish' deyin.")
print("- Çıkmak için 'kendini kapat' diyebilirsiniz.")
print("--------------------------------------------------")

try:
    with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, device=None, dtype='int16', channels=1, callback=callback):
        while True:
            data = q.get()
            
            if active_rec.AcceptWaveform(data):
                res = json.loads(active_rec.Result())
                text = res.get("text", "")
                
                if text:
                    # Çift çıktıyı önlemek için Partial (Dinleniyor) kısmı silindi ve '\n' kaldırıldı.
                    print(f"[{current_lang}] {text}")

                    cleaned_text = clean_text(text)
                    words = cleaned_text.split()

                    if current_lang == "TR":
                        for trigger in TRIGGERS_TO_EN:
                            if trigger in words:
                                active_rec = rec_en
                                current_lang = "EN"
                                print("---> DİL DEĞİŞTİRİLDİ: İNGİLİZCE (You can start speaking English)")
                                break
                    
                    elif current_lang == "EN":
                        for trigger in TRIGGERS_TO_TR:
                            if trigger in words:
                                active_rec = rec_tr
                                current_lang = "TR"
                                print("---> DİL DEĞİŞTİRİLDİ: TÜRKÇE (Türkçe konuşmaya başlayabilirsiniz)")
                                break
                    
                    if "kendini kapat" in text or "kill the program" in text:
                        print("SİSTEM KAPATILIYOR... / SHUTTING DOWN...")
                        sys.exit(0)

except KeyboardInterrupt:
    print("\nKullanıcı tarafından durduruldu.")
