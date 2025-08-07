import speech_recognition as sr

recognizer = sr.Recognizer()
microfone = sr.Microphone()

with microfone as source: # abrir e fechar microfone
    audio = recognizer.listen(source)

texto = recognizer.recognize_google(audio, language='pt-BR')
print(texto)