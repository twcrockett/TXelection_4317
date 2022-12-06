"""
author: @Taylor Crockett
"""

import pandas as pd
import numpy as np
import os
import js
import asyncio

directory = '_county-pbps'
merged = pd.DataFrame()

counties = {
    'collin.xlsx': 85,
    'dallas.xlsx': 113,
    'rockwall.xlsx': 397,
    'denton.xlsx': 121,
    'tarrant.xlsx': 439,
}

for file in os.listdir(directory):
    filename = os.path.join(directory, file)
    if os.path.isfile(filename):
        countycode = counties[file]
        toc = pd.read_excel(filename, sheet_name='Table of Contents', skiprows=3).set_index('Page')['Contest'].to_dict()
        sheet = 0
        for page, content in toc.items():
            if 'Governor' in content and 'Lieutenant' not in content:
                sheet = page
                # print(f'{filename}: sheet {page}')

        candidates = pd.read_excel(filename, sheet_name=sheet, skiprows=0, nrows=1).dropna(axis=1).values.tolist()[0]
        for i in range(len(candidates)):
            if candidates[i][1].isupper():
                candidates[i] = candidates[i][4:]

        df = pd.read_excel(filename, sheet_name=sheet, skiprows=2)
        headers = [h for h in df.head()]
        votes = df.set_index(headers[0]).filter(like='Total Votes').set_axis(candidates, axis=1, inplace=False)

        precincts = votes.index.tolist()
        for i in range(len(precincts)):
            if '-' in precincts[i]:
                precincts[i] = precincts[i][:-3]
            precincts[i] = f'{countycode}-{precincts[i]}'
        votes.index = precincts
        votes.index.names = ['CC-Precinct']

        votes.groupby('CC-Precinct').sum()

        merged = pd.concat([merged, votes], sort=False).fillna(0)

# ADD COLLIN

cfile = '_county-pbps\collin\collin.CSV'
collin = pd.read_csv(cfile)
collin['PRECINCT NAME'] = collin['PRECINCT NAME'].str.replace(' LB ', ' ').str.replace('PCT ', '85-')
collin = collin.groupby('PRECINCT NAME').sum().filter(['REP', 'DEM', 'LIB', 'GRN', 'Write-in'])
collin = collin.rename(
    columns={'REP': 'Greg Abbott', 'DEM': "Beto O'Rourke", 'LIB': 'Mark Tippetts', 'GRN': 'Delilah Barrios'})
collin.index.names = ['CC-Precinct']

merged = pd.concat([merged, collin], sort=False).fillna(0)

print(merged)
