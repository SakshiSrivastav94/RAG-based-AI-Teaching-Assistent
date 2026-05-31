# Speech to Text
import whisper
import json
model = whisper.load_model("large-v2", device="cpu")  # large-v2 model of whisper to translate non-english to english
result = model.transcribe(audio="unused/sample.mp3", 
                           language="hi",
                            task="translate",
                            fp16=False,
                            verbose=True,
                            word_timestamps=False)
# print(result)
# print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"], "end": segment["end"], "text": segment["text"]})

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks,f)