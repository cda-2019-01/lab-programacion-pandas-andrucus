##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

##respuesta 1
import pandas as pd
import numpy as np
df0 = pd.read_csv('tbl0.tsv', sep='\t')
df2 = pd.read_csv('tbl2.tsv', sep='\t')
llave = pd.merge(df0,df2, on='_c0')
respuesta = llave.groupby('_c1').agg({'_c5b': np.sum})
print(respuesta.iloc[:,0])


#respuesta 2

df2.groupby('_c0')['_c5b'].sum()

#Respuesta3

df2.groupby('_c5a')['_c5b'].sum()