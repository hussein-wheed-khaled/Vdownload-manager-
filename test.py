
"""from pytube import YouTube
import os
from pathlib import Path

link = input("Enter link here: ")

url = YouTube(link)

print("downloading....")

video = url.streams.get_highest_resolution()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

video.download(path_to_download_folder)
print("Downloaded! :)")"""
import os
import moviepy.editor
from tkinter.filedialog import *

#video=askopenfilename()


#video=moviepy.editor.VideoFileClip(video)
#audio=video.audio
#audio.write_audiofile("mp3\\"+str("ffffff.mp3"))
if os.path.exists("mp3\\" +"MrKitty - After Dark"+".mp4"):
 os.remove("mp3\\" +"MrKitty - After Dark"+".mp4")
