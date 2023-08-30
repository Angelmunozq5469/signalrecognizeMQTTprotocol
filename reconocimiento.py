# Importar libreria
import IPython.display as ipd # Para reproducir audio y videos en Jupyter Notebook
ipd.display( ipd.VimeoVideo("112133045"))

import speech_recognition as sr
print( f'La version de speech recognition es: {sr.__version__}')

# la clase que permite el uso de los sitemas de traduccion son Recognizer class.
r = sr.Recognizer()

# se utiliza el metodo record para cargar el archivo de audio
harvard = sr.AudioFile('/Users/angelemilio/Downloads/audio_prueba.wav') # cargar el archivo de audio
with harvard as source:
    #audio1 = r.record(source,duration=10) #Tomar los primeros 8 segundos
    audio1 = r.record(source) #Leer todo el archivo de audio
    
ipd.Audio('/Users/angelemilio/Downloads/audio_prueba.wav') # escuchar archivo de audio   

type(audio1)

# Convertir el habla en texto
print(r.recognize_google(audio1, language='es-CO'))



