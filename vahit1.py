# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:47:17 2022

@author: emrehan
"""

import pandas as pd
import seaborn as sns
titanic=sns.load_dataset("titanic")
titanic.head()

titanic.groupby("sex")["survived"].mean()

titanic.groupby(["sex","class"])["survived"].aggregate("mean").unstack()

titanic.groupby(["sex","class"])["survived"].aggregate("mean")

titanic.pivot_table("survived",index="sex",columns="class")

age=pd.cut(titanic["age"],[0,18,50,90])

titanic.groupby(age).count()

titanic.pivot_table("survived",["sex",age],"class")


df1=pd.read_csv("ornekcsv.csv")

df1=pd.read_csv("ornekcsv.csv",sep=";")

df2=pd.read_csv("duz_metin.txt")

df3=pd.read_excel("ornekx.xlsx")


