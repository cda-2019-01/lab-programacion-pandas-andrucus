##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
df0 = pd.read_csv('tbl0.tsv', sep='\t')
df0['suma'] = df0['_c0'] + df0['_c2']