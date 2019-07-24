#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:21:08 2019

@author: richardlee
"""

string = "3+4*4+12/483"
operator_list = "+-*/"
result = []
    

stack =""
for char in string:
    if char not in operator_list:
        stack = stack + char
    else:
        if stack =="":
            stack = stack +char
        else:
            result.append(stack)
            result.append(char)
            stack =""
result.append(stack)
final = "".join(result[::-1])
    