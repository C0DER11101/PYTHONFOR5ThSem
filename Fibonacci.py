#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:17:20 2022

@author: priyanuj
"""

size=int(input("enter size of the array: "));    
    
first=0;
second=1;

print("\n\nhere is the fibonacci series:\n\n");
a=list();

a.append(first);
a.append(second);
for i in range(0, size-2):
    third=first+second;
    a.append(third);
    first=second;
    second=third;
    
    
print(a)