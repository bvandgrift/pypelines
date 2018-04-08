#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
from pipeline import Pipeline

if __name__ == '__main__':

    pipeline = Pipeline()
    with open('alevo.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            if row:
                trow = row[:100]
                frame = pipeline.process(trow)
                print(frame)
                plt.plot(range(0, len(trow)),          trow,          'r--', linewidth=1)
                plt.plot(range(0, len(frame['data'])), frame['data'], 'b-',  linewidth=1)
                plt.show()
