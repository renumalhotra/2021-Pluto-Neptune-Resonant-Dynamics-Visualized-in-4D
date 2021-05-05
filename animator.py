import imageio
import pandas as pd
data = pd.read_csv('rebound_data.txt',sep = ' ')
fps = 30 # frames per second can be changed depending on user preference

filenames=['tmp_frames/_tmp%3i.jpg'%i for i in range(len(data))]
images = []

for i, filename in enumerate(filenames):
    images.append(imageio.imread(filename))

imageio.mimsave('xy_movie.mp4',images,fps=fps) # be sure to change the filename when running a new animation to avoid overwriting files

import os
os.system('rm tmp_frames/_tmp*.jpg')