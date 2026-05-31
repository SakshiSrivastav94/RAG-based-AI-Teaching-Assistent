# This file takes hours to run  ..............

import whisper
import json
import os

# whisper is a speech recognition model developed by OpenAI that can transcribe audio into text. It is designed to be highly accurate and can handle a wide range of languages and accents. The model is based on a transformer architecture and has been trained on a large dataset of audio and text.

model = whisper.load_model("large-v2")   # takes max time to load this model

audios = os.listdir("audios")

for audio in audios: 
    number = audio.split("_")[0]
    title = audio.split("_")[1][:-4]
    print(number, title)
    result = model.transcribe(audio = f"Audios/{audio}", 
    # result = model.transcribe(audio = f"Audios/sample.mp3", 
    language="hi",
    task="translate",
    word_timestamps=False )

    chunks = []

    for segment in result["segments"]:
        chunks.append({"number": number, "title":title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}


        # dumping the chunks with metadata into json file in jsons folder
        with open(f"jsons/{audio}.json", "w") as f:
            json.dump(chunks_with_metadata,f)    