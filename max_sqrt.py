#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:04:23 2019

@author: richardlee
"""




import math
a= 6000
b= 8000
l=[a,b]

def sqrt_list(a,b):
    sqrt = list(map(int,[math.sqrt(a),math.sqrt(b)]))
    return [i for i in range(sqrt[0],sqrt[1]+1)]



count=0


while l:
    temp = sqrt_list(l[0],l[-1])
    if len(temp)==1:
        break
    l=temp
    count+=1

  
if count ==0:
    result = 1
else:
    result = l[-1]
    
    for i in range(count):
        result= result **2
    
result

