##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 

import pandas as pd
df0 = pd.read_csv('tbl0.tsv', sep='\t')
df1 = pd.read_csv('tbl1.tsv', sep='\t')
df2 = pd.read_csv('tbl2.tsv', sep='\t')

df0.groupby('_c1').count()['_c0']