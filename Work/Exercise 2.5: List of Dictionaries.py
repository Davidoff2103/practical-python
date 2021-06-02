# report.py

import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name' : row[0], 'shares': int(row[1]), 'price' : float(row[2])}
            portfolio.append(holding)
        
    return portfolio

print(read_portfolio('Data/portfolio.csv'))