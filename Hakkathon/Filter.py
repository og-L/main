# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:10:02 2020

@author: Dr. Spaghetto
"""

import pandas as pd
losunBensin = 2.31
losunDisel = 2.68
pd.set_option('mode.chained_assignment', None)
gogn = pd.read_excel('Eldsneytisgogn.xlsx')

siud_gogn = gogn.loc[(gogn['TegundNr'] == 1)]
siud_gogn = siud_gogn.drop(columns=['NotflNr'])
siud_gogn = siud_gogn.drop(columns=['NotFlHeiti'])
siud_gogn = siud_gogn.drop(columns=['TegundHeiti'])
siud_gogn = siud_gogn.drop(columns=['EldsnTegNr'])
siud_gogn = siud_gogn.drop(columns=['Frumorka'])


bensingogn = siud_gogn.to_csv('bensingogn.csv', index = True)


bensin = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] == 'Bensín')]
bensin['Losun (kg)'] = bensin['Notkun']*losunBensin


disel = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] == 'Dísilolía')]
disel['Losun (kg)'] = disel['Notkun']*losunDisel



annad = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] != 'Bensín') & (siud_gogn['EldsnTegHeiti'] != 'Dísilolía') & (siud_gogn['EldsnTegHeiti'] != 'Rafmagn')]
annad['Losun (kg)'] = annad['Notkun']*0



#print(bensin.iat[100,4])


lastar = 0
ar = 0
input_data = []
ars = []
arsum = 0
for x in range(0,bensin.shape[0]):
    ar = bensin.iat[x,0]
  #  print(ar)
    if lastar == ar:
        arsum = bensin.iat[x,bensin.shape[1]-1]+ arsum
    elif x == 0:
        lastar = ar
        arsum = bensin.iat[x,bensin.shape[1]-1]
    else:
        ars.append(lastar)
        lastar = ar
        input_data.append(arsum)
        arsum = bensin.iat[x,bensin.shape[1]-1]
ars.append(lastar)
input_data.append(arsum)

d= {"Ar": ars,"Losun (kg)": input_data}
df = pd.DataFrame(data = d)

df.to_csv('Samtals_bensin.csv', index = True)
bensin.to_csv('bensin.csv', index = True)
disel.to_csv('disel.csv', index = True)
annad.to_csv('annad.csv', index = True)