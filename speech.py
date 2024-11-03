import pyttsx3

# Inisialisasi mesin TTS
engine = pyttsx3.init()

# Fungsi untuk menghasilkan suara dari teks
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Contoh penggunaan
gesture = "A"  # Misalnya, deteksi gestur "A"
speak(gesture)  # Akan menghasilkan suara "A"