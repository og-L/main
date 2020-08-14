# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:00:12 2020

@author: Dr. Spaghetto
"""


import pandas as pd

df = pd.read_csv('bensin.csv')
losun = 2.3


df['Losun (kg)'] = df['Notkun']*losun

print(df.head(10))
