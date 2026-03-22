import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ENOVA is listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            return r.recognize_google(audio).lower()
        except:
            return ""