##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 


import pandas as pd
df1 = pd.read_csv('tbl1.tsv', sep='\t')

unicos = df1['_c4'].unique()
x =[]
for letra in unicos:
    x.append(letra.upper())
x = sorted(x)
x
