import whisper
#from pydub import AudioSegment
import os
# Afficher la valeur de la variable PATH
path_value = os.environ.get('PATH')
print(path_value)
#import ffmpeg
file_path = "jul_tchikita.mp3"

if os.path.exists(file_path):
    print("Le fichier existe.")
else:
    print("Le fichier n'existe pas.")


model = whisper.load_model("base")
print("ok")
result = model.transcribe("jul_tchikita.mp3",fp16=False)
print(result["text"])
print("ok")