# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=False, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue

            # Filter the row if specific columns were selected 
            if select:
                row = [ row[index] for index in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row) 
            records.append(record)

        return records