#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0, './lib')
import plotter

ani = plotter.SubplotAnimation()
#ani.save(filename='sim.mp4',fps=30,dpi=300)
tmin = 0  # secs
tmax = 3600 # secs
Dt   = 0.01
t = np.linspace(tmin, tmax, (tmax-tmin)/Dt)
x = 2*np.cos(2 * np.pi * t)
y = np.sin(2 * np.pi * t)

try:
    for i in range(1,1000):
        ani.draw_frame(i, t[i], x[i], y[i])
except (KeyboardInterrupt, SystemExit):
    quit()