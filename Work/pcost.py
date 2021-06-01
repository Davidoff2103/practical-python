# pcost.py

suma = 0

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
for line in f:
    row = line.split(',')
    shares = int(row[1])
    purchase = float(row[2])
    suma = suma + shares * purchase

f.close()

print(f'The cost to purchase all of the shares in the portfolio is {suma}€')