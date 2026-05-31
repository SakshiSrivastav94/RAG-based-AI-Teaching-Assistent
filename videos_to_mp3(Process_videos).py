# convert the webm(videos) to mp3(Audios)
import os
import subprocess
files = os.listdir("Videos")
# print(files)
for file in files:
    # print(file)
    tutorial_number = file.split("[")[0].split(" #")[1]
    # print(tutorial_number)
    file_name = file.split("｜")[0]
    print(tutorial_number, file_name)
    # mp3 file creation
    subprocess.run(["ffmpeg", "-i", f"Videos/{file}", f"Audios/{tutorial_number}_{file_name}.mp3"])  # here, Videos/{file} --> input,  Audios/{tutorial_number}_{file_name}.mp3 --> output 