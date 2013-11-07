Pygmaps-extended is a Python wrapper for the Google Maps JavaScript API V3.
This library builds upon the original [Pygmaps](https://code.google.com/p/pygmaps/) by Yifei Jiang. This includes support for Google Earth plugin integration, and additional utility functions.

This extension is not backwards compatibile with the original pygmaps, as some functions names have been changed.

## Features:

- Plotting of simple markers, grids, polygons, and polylines
- Plotting of variable color polylines based on scalar data

## Simple example:

## Advanced example:

`example.py` produces a map based on the design of a 3U CubeSat mission.
It will plot the trajectory of the satellite over the course of half of a day, one month following its launch. The path of the satellite is colored based on its data transmission rate to the ground station, in Ann Arbor MI.

[Click to see the result](http://rawgithub.com/thearn/pygmaps/master/example.html)