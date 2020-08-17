# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:10:02 2020

@author: Dr. Spaghetto
"""

import pandas as pd
### Vantar góða heimild fyrir þessar tölur
losunBensin = 2.31
losunDisel = 2.68
losunRaf = 0

pd.set_option('mode.chained_assignment', None)

### Lesum inn gögn og fjarlægjum dálka sem við þurfum ekki
gogn = pd.read_excel('Eldsneytisgogn.xlsx')


siud_gogn = gogn.loc[(gogn['TegundNr'] == 1)]
siud_gogn = siud_gogn.drop(columns=['NotflNr'])
siud_gogn = siud_gogn.drop(columns=['NotFlHeiti'])
siud_gogn = siud_gogn.drop(columns=['TegundHeiti'])
siud_gogn = siud_gogn.drop(columns=['EldsnTegNr'])
siud_gogn = siud_gogn.drop(columns=['Frumorka'])


#bensingogn = siud_gogn.to_csv('bensingogn.csv')


### Skilgreinum fall sem við notum til þess að sameina gögn frá sama ári
def heildarnotkun(gogn):
    #print(gogn)
    lastar = 0 
    ar = 0 
    input_data = [] 
    ars = [] 
    arsum = 0 
    for x in range(0,gogn.shape[0]): 
        ar = gogn.iat[x,0] 
        if lastar == ar: 
            arsum = gogn.iat[x,gogn.shape[1]-1]+ arsum 
        elif x == 0: 
            lastar = ar 
            arsum = gogn.iat[x,gogn.shape[1]-1] 
        else: 
            ars.append(lastar) 
            lastar = ar 
            input_data.append(arsum) 
            arsum = gogn.iat[x,gogn.shape[1]-1] 
 
    d= {"Ar": ars,"Losun (kg)": input_data} 
    df = pd.DataFrame(data = d)
    return df

### Útbúum sér gögn fyrir þrjár tegundir af eldsneyti í bifreiðar: Bensín, dísilolíu og rafmagn

bensin = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] == 'Bensín')]
bensin['Losun (kg)'] = bensin['Notkun']*losunBensin
bensinTot = heildarnotkun(bensin)
bensinTot.to_csv('bensin.csv')


disel = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] == 'Dísilolía')]
disel['Losun (kg)'] = disel['Notkun']*losunDisel
diselTot = heildarnotkun(disel)
diselTot.to_csv('disel.csv')


raf = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] == 'Rafmagn')]
raf['Losun (kg)'] = raf['Notkun']*losunRaf
rafTot = heildarnotkun(raf)
rafTot.to_csv('raf.csv')


### Höfum hér safn fyrir aðrar tegundir af eldnsyti (s.s. metan og steinolíu en við notum þau gögn ekki eins og er)

annad = siud_gogn.loc[(siud_gogn['EldsnTegHeiti'] != 'Bensín') & (siud_gogn['EldsnTegHeiti'] != 'Dísilolía') & (siud_gogn['EldsnTegHeiti'] != 'Rafmagn')]
annad['Losun (kg)'] = annad['Notkun']*0
annadTot = heildarnotkun(annad)
annadTot.to_csv('annad.csv')



