##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 


import pandas as pd

df2 = pd.read_csv('tbl2.tsv', sep='\t')

df2['_c5'] = df2['_c5a'] + ':' + df2['_c5b'].astype('str')
dftabla = df2.groupby('_c0')['_c5'].apply(list)

dfaux = pd.DataFrame()
dfaux['col1'] = dftabla.keys()
dfaux['col2'] = [x for x in dftabla]
dfaux['col2'] = [",".join(str(a) for a in sorted(x)) for x in dfaux['col2']]
dfaux