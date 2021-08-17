from PIL import Image
import glob
import moviepy.editor as mp
import numpy as np
import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

image_list = []
i = 0
clips = []
widths = []
filenames = []
for filename in glob.glob('./gif/9/*.gif'):
    clip = mp.VideoFileClip(filename)
    filenames.append(path_leaf(filename[0:-4]))
    widths.append(clip.size[0])
    clips.append(clip)

for clip in clips:
    # clip.resize(width = np.max(widths))
    clip.write_videofile('./gif/9.9/' + filenames[i] + ".mp4")
    i = i + 1