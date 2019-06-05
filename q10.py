##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas as pd
df1 = pd.read_csv('tbl1.tsv', sep='\t')

dfagrupa = df1.groupby('_c0')['_c4'].apply(list)
df = pd.DataFrame()
df['llave'] = dfagrupa.keys()
df['listado'] = [x for x in dfagrupa]
df['listado'] = [":".join(str(a) for a in sorted(a)) for a in df['listado']]
df