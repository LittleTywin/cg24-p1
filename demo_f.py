import numpy as np

data = np.load("hw1.npy",allow_pickle=True).item(0)

faces = data["faces"]
vertices = data["vertices"]
vcolors = data["vcolors"]
vdepth = data["depth"]
