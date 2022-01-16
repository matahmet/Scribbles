# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:45:43 2022

@author: USER07
"""

import numpy as np

a=np.array([1,2,3])
b=np.array([1,2,3.14])
c1=np.zeros(10)
c2=np.zeros(10,dtype=int)
c3=np.zeros((4,4))
c4=np.zeros((2,2,2),)
c5=3*np.ones((4,4))
c5
c3
c6=np.full((2,3),4)
c7=np.arange(2,16,3)
c8=np.linspace(0,1,11)
c9=np.random.normal(20,3,100)
c10=np.random.normal(20,3,(4,4))
c11=np.random.randint(0,16,(4,4))

x=np.array([1,2,3])
y=np.array([1,2,3])+12
z=np.concatenate([x,y])
z1=np.reshape(z,(2,3))
z1
z2,z3,z4=np.split(z,(2,4))

np.sort(c9)

5*np.array([1, 2,3])




d=np.arange(0,30,3)
d[d<16]





























