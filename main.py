from moviepy.editor import VideoFileClip #pip install moviepy

clip = VideoFileClip("vid.mp4") #Adding The Video File

clip.write_gif("myd.gif", fps=6) #Naming The Gif And Setting Up The FPS Value 
