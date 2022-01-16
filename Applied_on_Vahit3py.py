# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:46:27 2022

@author: USER07
"""

import seaborn as sns

df=sns.load_dataset("planets")
df
df.head()
df.shape
df.shape[0]
df.mean()
df["orbital_period"].mean()
df["mass"].std()
df["mass"].mean()
df.describe()
df.describe().T
df.dropna().describe()


df.groupby("method").count()
df.groupby("method")["orbital_period"].mean()
df.groupby("method")["orbital_period"].describe()
df.groupby("method")["orbital_period"].std()


import pandas as pd
df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,262,111,969]},
                   columns = ['gruplar', 'degisken1', 'degisken2'])
df

import numpy as np

df.groupby("gruplar").aggregate([min,np.median,max,"count"])


def filter_func(x):return x["degisken1"].std()<9

df.groupby("gruplar").filter(filter_func)

df_a=df.iloc[:,1:3]

df_a.transform(lambda x: x-x.mean())

df_a = df.iloc[:,1:3]

df_a.transform(lambda x: (x-x.mean()) / x.std())

df.groupby("gruplar").apply(lambda x:x.max()-x.min())

def myrange(x):return x.max()-x.min()

df.groupby("gruplar").apply(myrange)






