# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:10:02 2020

@author: Dr. Spaghetto
"""

import pandas as pd
losunBensin = 2.31
losunDisel = 2.68

gogn = pd.read_excel('Eldsneytisgogn.xlsx')

siud_gogn = gogn.loc[(gogn['TegundNr'] == 1)]

#print(siud_gogn.head(25))

bensingogn = siud_gogn.to_csv('bensingogn.csv', index = True)


bensin = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] == 'Bensín')]
bensin['Losun (kg)'] = bensin['Notkun']*losunBensin
bensin.to_csv('bensin.csv', index = True)

disel = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] == 'Dísilolía')]
disel['Losun (kg)'] = disel['Notkun']*losunDisel
disel.to_csv('disel.csv', index = True)

annad = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] != 'Bensín') & (siud_gogn['EldsnTegHeiti'] != 'Dísilolía') & (siud_gogn['EldsnTegHeiti'] != 'Rafmagn')]
annad['Losun (kg)'] = annad['Notkun']*0
annad.to_csv('annad.csv', index = True)