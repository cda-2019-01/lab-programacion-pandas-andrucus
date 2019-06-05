##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
df0 = pd.read_csv('tbl0.tsv', sep='\t')
df0['ano'] = [x.split('-')[0] for x in df0['_c3']]