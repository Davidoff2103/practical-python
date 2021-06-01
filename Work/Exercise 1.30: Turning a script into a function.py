def portfolio_cost(filename):
    suma = 0
    f = open(filename, 'rt')
    next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        purchase = float(row[2])
        suma = suma + shares * purchase

    f.close()

    return suma

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)