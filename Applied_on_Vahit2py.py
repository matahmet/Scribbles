# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:19:06 2022

@author: USER07
"""

import pandas as pd
a=pd.Series([1,4,5,2,7])
a.index
a.values
b=pd.Series([1,4,5,2,7],index=["a","b","c","d","e"])
b
b['b']

'b' in b

1 in b

list(b.items())

import numpy as np
m=np.random.randint(1,30,size=(10,3))
df=pd.DataFrame(m,columns=["v1","v2","v3"])
list(df.index)
df.loc[0:3,"v3"]
df.iloc[0:3]["v3"]
df[df.v1>10]
df[df.v2<10]
df[df.v3==10]

df[(df.v1<10)|(df.v2>20)]

df1 = pd.DataFrame({'calisanlar': ['Ali', 'Veli', 'Ayse', 'Fatma'],
                    'grup': ['Muhasebe', 'Muhendislik', 'Muhendislik', 'İK']})


df2 = pd.DataFrame({'calisanlar': ['Ayse', 'Ali', 'Veli', 'Fatma'],
                    'ilk_giris': [2010, 2009, 2014, 2019]})


pd.merge(df1,df2,on="calisanlar")


