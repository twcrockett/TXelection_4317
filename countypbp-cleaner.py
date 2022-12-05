"""
author: @Taylor Crockett
"""

import pandas as pd
import numpy as np
import os
# import geopandas as gp

directory = '_county-pbps'

for file in os.listdir(directory):
    filename = os.path.join(directory, file)
    if os.path.isfile(filename):
        toc = pd.read_excel(filename, sheet_name='Table of Contents', skiprows=3).set_index('Page')['Contest'].to_dict()
        sheet = 0
        for page, content in toc.items():
            if 'Governor' in content and 'Lieutenant' not in content:
                sheet = page
                print(f'{filename}: sheet {page}')
        candidates = pd.read_excel(filename, sheet_name=sheet, skiprows=0, nrows=1).dropna(axis=1).values.tolist()[0]

        # headers = [0]
        # for c in range(len(candidates)):
        #     h = (c + 1) * 4 + 1
        #     headers.append(h)
        # print(headers)

        df = pd.read_excel(filename, sheet_name=sheet, skiprows=2)
        headers = [h for h in df.head()]
        votes = df.set_index(headers[0]).filter(like='Total Votes').set_axis(candidates, axis=1, inplace=False)

        # df[0] = np.where(pd.Series(df.index).astype(str).str.contains('-'), df[0], df[0].str[:-3].astype(str))

        # if '-' in df.iat[0, 1]:
        #     df[0] = df[0][:-1].str[:-3].astype(str)

        # df[0].mask('-' in df[0], df[0][:-1].str[:-3].astype(str), inplace=True).groupby('Precinct').sum()
        print(votes)
