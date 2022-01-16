# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:52:28 2022

@author: emrehan
"""

values = ["a", "b", "c"]

for value in values:
     print(value)
     
index = 0

for value in values:
    print(index, value)
    index += 1
    

for index in range(len(values)):
    value = values[index]
    print(index, value)
    
for count, value in enumerate(values):
    print(count, value)

for count, value in enumerate(values):
    print(value)
    
for count, value in enumerate(values):
    print(count)    
    

a=[0,1,3,0]
b=["a",'x','x','b',"k"]

for count,value in enumerate(a):
    print(value)
    print(b[count])



    
import numpy as np

m=np.zeros((4,4))
m[1,a]=1
    
m[0,[1,3]]=10  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    