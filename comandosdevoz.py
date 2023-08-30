import speech_recognition as sr
from transcribir import start,stop

def reconocimientodevoz():
    global i
    r = sr.Recognizer()
    trigger_word = "comenzar"
    trigger_word2 = "para"
    i = 0

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Esperando Comando de voz")

            try:
                audio = r.listen(source)
                text = r.recognize_google(audio, language="es-CO").lower()
                #recognize_sphinx esta libreria seria utilizada de manera offline
                if trigger_word in text:
                    start(i)

                elif trigger_word2 in text:
                    stop(i)
                    break
                  

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Error:", e)
