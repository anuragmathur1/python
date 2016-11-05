#!/usr/bin/python3
import csv

with open('portfolio.csv','r') as f:
    rows = csv.reader(f)
    headers = next(rows) ## skip the header
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        total += row[2] * row[3]

print('Total cost:', total)

