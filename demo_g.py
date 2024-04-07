import numpy as np
import os
import tripaint as tp
import matplotlib
from matplotlib import pyplot as plot
matplotlib.use('TkAgg')

#load data
data = np.load("hw1.npy", allow_pickle=True).item(0)
vertices = data["vertices"]
vcolors = data["vcolors"]
depth = data["depth"]
faces = data["faces"]

gouraud_img = tp.render_img(faces, vertices, vcolors, depth,"gouraud")
# plot.imshow(gouraud_img)
# plot.show()

dir = "output_images"
gouraud_file = "gouraud.png"
path = os.path.join(os.getcwd(),dir)
if not os.path.exists(path):
    os.makedirs(path)
plot.imsave(dir+'/'+gouraud_file,gouraud_img)
