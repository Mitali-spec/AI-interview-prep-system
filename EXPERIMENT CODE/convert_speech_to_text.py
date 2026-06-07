from faster_whisper import WhisperModel
model=WhisperModel("base")  #balanced size of whisper
segments, info=model.transcribe(r"c:\Users\mitaa\Downloads\sundari.mp3")
for s in segments:
    print(s.text)
