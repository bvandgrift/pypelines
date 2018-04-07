#!/usr/bin/env python3

import csv
from config import config
from toolz.functoolz import thread_last

if __name__ == '__main__':

    with open('test1.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        results = []
        for row in reader:
            if row:
                results.append(list(thread_last(row, *config.filters)))
        print(results)
