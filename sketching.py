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