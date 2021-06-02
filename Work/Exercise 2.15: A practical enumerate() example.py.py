import sys

def portfolio_cost(filename):
    rows = open(filename, 'rt')
    next(rows)
    suma = 0
    for rowno, row in enumerate(rows, start=1):
        try:
            row = row.split(',')
            shares = int(row[1])
            purchase = float(row[2])
            suma = suma + shares * purchase
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    rows.close()

    return suma

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)