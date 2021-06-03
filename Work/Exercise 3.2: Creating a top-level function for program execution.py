import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name' : row[0], 'shares': int(row[1]), 'price' : float(row[2])}
            portfolio.append(holding)
        
    return portfolio


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        #se coge el precio del diccionario de precios en la que coincida el nombre
        current_price = prices[stock['name']]
        #se resta del precio anterior el precio actual (que se saca de la 'columna' price de la fila stock de la lista portfolio)
        change = current_price - stock['price']
        #se guarda en una variable name, shares, current_price y change
        summary = (stock['name'], stock['shares'], current_price, change)
        #se añade a la lista
        rows.append(summary)
    return rows

  
def portfolio_report(portfoliofile, pricefile):        
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(portfolio,prices)

    # Print it out
    print_report(report)


def print_report(report):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')