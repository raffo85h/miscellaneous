# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 18:15:51 2014

@author: raffaelerainone
"""

#Standard bubble sort algorithm.

def bubble(list):
    for j in range(len(list)):
        for i in range(len(list)-j-1):
            if list[i+1]<list[i]:
                T = list[i]
                list[i] = list [i+1]
                list[i+1] = T
    return list