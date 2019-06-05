##
## Imprima la suma de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

import pandas as pd
df0 = pd.read_csv('tbl0.tsv', sep='\t')
df0.groupby('_c1').sum()['_c2']