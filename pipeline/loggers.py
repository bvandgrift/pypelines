import csv
import json


def lDebug(frame):
    print(frame)
    return frame


def lCSV(frame):
    outfile = frame['props'].get('out.csv') or 'out.csv'
    with open(outfile, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(frame['data'])
    return frame


def lRawCSV(frame):
    outfile = frame['props'].get('raw.csv') or 'raw.csv'
    with open(outfile, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(frame['data'])
    return frame


def lMetaCSV(frame):
    outfile = frame['props'].get('meta.csv') or 'meta.csv'
    with open(outfile, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(frame['summary'].values)
    return frame


def lJSON(frame, dargs={}):
    outfile = frame['props'].get('out.json') or 'out.json'
    with open(outfile, 'a') as f:
        json.dump(frame, f)
    return frame
