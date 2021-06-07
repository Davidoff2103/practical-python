class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings'
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single ro of table data
        '''
        raise NotImplementedError()