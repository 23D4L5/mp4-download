import moviepy.editor
from tkinter.filedialog import *

vid = askopenfile()
video = moviepy.editor.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile('dmo.mp3')

print('Extracted audio from mp4 file successfully.')