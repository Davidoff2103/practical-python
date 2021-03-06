# pcost.py

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    suma = 0
    f = open(filename, 'rt')
    next(f)
    for line in f:
        row = line.split(',')
        try:
            shares = int(row[1])
            purchase = float(row[2])
            suma = suma + shares * purchase
        # This catches errors in int() and float() conversions above
        except ValueError:
            print('Bad row:', row)
    f.close()
    return suma

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)