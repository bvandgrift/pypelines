import csv
import json


def lCSV(data, dargs={}):
    outfile = dargs.get('outfile') or 'out.csv'
    with open(outfile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return data


def lJSON(data, dargs={}):
    outfile = dargs.get('outfile') or 'out.json'
    with open(outfile, 'w') as f:
        json.dump(data, f)
    return data
