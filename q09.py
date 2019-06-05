##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd
df0 = pd.read_csv('tbl0.tsv', sep='\t')
dftabla= df0.groupby('_c1')['_c2'].apply(list)

df = pd.DataFrame()
df['_c1'] = dftabla.keys()
df['_c2'] = [numero for numero in dftabla]
df['_c2'] = [":".join(str(v) for v in sorted(numero)) for numero in df['_c2']]
df
