#
# Collect data from csv files
# 2021/2/22 koizumi
#
import numpy as np
import pandas as pd
import glob
import datetime

files = glob.glob('Humax*.csv')

parserfnc = lambda x : datetime.datetime.strptime(x, '%a %b %d %H:%M:%S %Y')

df = None
for file in files:
    ddf = pd.read_csv(file, parse_dates=['time'], date_parser=parserfnc)
    if df is None:
        df = ddf.copy()
    else:
        df = pd.concat([df, ddf], sort=False)

df.drop_duplicates(subset='time', inplace=True)
df.sort_values(by='time', inplace=True)
df.reset_index(inplace=True, drop=True)
df = df[['time', 'priority', 'description']]

df.to_excel('HumaxLog.xlsx', index=None)
