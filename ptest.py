#!/usr/bin/env python3

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from pipeline import Pipeline

patch = None

fig = plt.figure()
ax1 = plt.axes(xlim = (0,98), ylim = (20,300))
line, = ax1.plot([],[], lw=1, color="red")
plt.xlabel("mm")
plt.ylabel("microns")

plotlays, plotcols = [2], ['red', 'blue']
lines=[]

for index in range(2):
    lobj = ax1.plot([],[],lw=2, color=plotcols[index])[0]
    lines.append(lobj)


csvfile = open('csv/test3.csv', newline='', encoding='utf-8')
reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
pipeline = Pipeline()

x = range(98)

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    row = next(reader)
    if row:
        trow = row[:98]
        frame = pipeline.process(trow)
        datas = [trow, frame['data']]
        for lnum, line in enumerate(lines):
            line.set_data(x, datas[lnum])
    return lines

ani = FuncAnimation(fig, animate, init_func=init, interval=200, blit=True, frames=100)

plt.show()

csvfile.close()

"""

if __name__ == '__main__':

    csvfile = open('csv/alevo.csv', newline='', encoding='utf-8')
    fig, ax = plt.subplots()

    pipeline = Pipeline()
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        if row:
            trow = row[:100]
            frame = pipeline.process(trow)
            print(frame)
            plt.plot(range(0, len(trow)),          trow,          'r--', linewidth=1)
            plt.plot(range(0, len(frame['data'])), frame['data'], 'b-',  linewidth=1)
            plt.show()

    csvfile.close()

"""
