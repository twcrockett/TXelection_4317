"""
author: @Taylor Crockett
"""

import pandas as pd

filename = 'November 8 2022 General and Special Election Results Export.CSV'
df = pd.read_csv(filename)
df['PRECINCT NAME'] = df['PRECINCT NAME'].str.replace(' LB ', ' ')

df2 = df.groupby('PRECINCT NAME').sum()
print(df2)
