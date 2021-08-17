from PIL import Image
import glob
import moviepy.editor as mp
import random

list_of_clips = []
i = 0

for filename in glob.glob('./gif/9.9/*.mp4'): 

    clip = mp.VideoFileClip(filename)
    clipduration = (clip.duration)

    number_of_repeat = int(random.randrange(5, 10)/clipduration) + 1
    print(clipduration)
    print(number_of_repeat)
    for i in range(0, number_of_repeat):
        list_of_clips.append(clip)

# print(clips)
final = mp.concatenate_videoclips(list_of_clips, method='compose')
final.write_videofile("9.mp4")