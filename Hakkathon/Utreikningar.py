# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:25:59 2020

@author: Dr. Spaghetto
"""
### Meðalkeyrsla íslendings á mánuði skv samgöngustofu
medalkeyrsla = 1065
### Viðmið á meðaleldsneytisnotkun (l/100 km) skv IEA (þyrftum að finna betri tölur en fundum hana ekki í bili)
eldsneytisnotkunBensin = 7.2
#eldsneytisnotkunDisel = 
### Losun skv https://www.nrcan.gc.ca/sites/www.nrcan.gc.ca/files/oee/pdf/transportation/fuel-efficient-technologies/autosmart_factsheet_6_e.pdf
losunBensin = 2.29
losunDisel = 2.66
### Kostnaður fyrir eldsneyti (viðmið útfrá verðum 18. ágúst)
kostnBensin = 200
kostnDisel = 195

### Meðallosun fyrir bensínbíl
losunBensin = medalkeyrsla * eldsneytisnotkunBensin * 0.01 * losunBensin
### Meðallosun fyrir dísilbíl
losunDisel = medalkeyrsla * eldsneytisnotkunBensin * 0.01 * losunDisel
### Meðalkostnaður
kostnadurBensin =  medalkeyrsla * eldsneytisnotkunBensin * 0.01 * kostnBensin
kostnadurDisel =  medalkeyrsla * eldsneytisnotkunBensin * 0.01 * kostnDisel

print(f'Meðal íslendingur á bensínbíl losar {int(round(losunBensin))} kg af CO2 á mánuði'
      f' og borgar {int(kostnadurBensin)}kr fyrir bensín') 
print(f'Meðal íslendingur á díselbíl losar {int(round(losunDisel))} kg af CO2 á mánuði'
      f' og borgar {int(kostnadurDisel)} fyrir dísil')