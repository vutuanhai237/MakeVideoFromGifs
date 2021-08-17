# Produce video from gifs with python

How to use this repository?

Make sure that you have moviepy package. (pip install moviepy). Then:

1. Collect your gifs in specific folder

2. Rename file names to avoid long path if you need (using change_file_name.py). Function changeAllFileNameSuffer() will help you suffer the files.

3. Convert all gifs into .mp4 file by using gif_to_mp4.py, umcomment line 22 if you want all gifs have the same resolution.
 
4. Combine them all by using concate.py. Here you can custom the duration of each gif, or random value as I did.
