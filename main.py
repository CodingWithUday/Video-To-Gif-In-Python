from moviepy.editor import VideoFileClip #pip install moviepy

clip = VideoFileClip("vid.mp4")

clip.write_gif("myd.gif", fps=6)