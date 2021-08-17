from moviepy.editor import *
videoclip = VideoFileClip("filename.mp4")
audioclip = AudioFileClip("audioname.mp3")
new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("new_filename.mp4")