#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 00:44:41 2019

@author: richardlee
"""
import time
start_time = time.time()
n=100000
l = [i for i in range(1,n+1)]

prime_list=[]


def prime(lis,n):
    for i in range(1,len(lis)):
        if n% lis[i]==0:
            return False
    else:
        return True

    
def six_digit(l):
    if l[0] ==1:
        prime_list.append(l[0])
        l.remove(l[0])    
    while l:
        prime_list.append(l[0])
        l=list(filter(lambda x : x%l[0]!=0,l))
    return prime_list

if n > 100000:
    prime_list = six_digit(l)
    
else:
    prime_list
print("--- %s seconds ---" % (time.time() - start_time))       

l = list(filter(lambda x: x%2!=0,l))

prime(prime_list,3)
l[0]