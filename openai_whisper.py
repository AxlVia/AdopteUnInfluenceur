#pip install openai-whisper

import whisper 

model = whisper.load_model("base")
result = model.transcribe("jul_tchikita",fp16=false)
print(result["text"])