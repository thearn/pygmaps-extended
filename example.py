import numpy as np
import pygmaps

data = np.loadtxt("cubesat.csv", delimiter=",")

path = data[:, :2]
data_rate = data[:, -1]

gmap = pygmaps.gmap(41, -88, zoom=2)
gmap.add_weighted_path(path, data_rate)
gmap.draw("example.html")
