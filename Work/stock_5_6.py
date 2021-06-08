class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares

    def __repr__(self):
        return (f'Stock({self.name!r}, {self.shares!r}, {self.price!r})')