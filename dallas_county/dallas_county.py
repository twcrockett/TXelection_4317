"""
author: @Taylor Crockett
"""

import pandas as pd

filename = '221108 General and Joint.xlsx'
df = pd.read_excel(filename, sheet_name='8')
precinct_totals = df.filter(['Precinct', 'Total Votes REP', 'Total Votes DEM', 'Total Votes LIB', 'Total Votes GRN',
                             'Total Votes W-I', 'Total'], axis=1)
precinct_totals = precinct_totals.rename(
    columns={'Total Votes REP': 'REP', 'Total Votes DEM': 'DEM', 'Total Votes LIB': 'LIB', 'Total Votes GRN': 'GRN',
             'Total Votes W-I': 'Write-in'})
precinct_totals['Precinct'] = 'PCT ' + precinct_totals['Precinct'][:-1].str[:-3].astype(str)
merged = precinct_totals.groupby('Precinct').sum()
print(merged)
