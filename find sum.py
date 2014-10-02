# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 11:13:45 2014

@author: Raffo
"""
#Given two sorted arrays of integers, find the pair of indices (one into each array)
#which identify elements which sum to a given integer, if any such pair exists.

#Input
#l1 = first sorted array of integers;
#l2 = second sorted array of integers;
#summ = 'given integer'

#Output:
#Array with couples of integers [[i1,j1], [i2,j2],..] such that
# li[i1] + l2[j2] = summ, etc.

def find(l1,l2,summ):
#First we check if the number can actually be the sum of two integers in the sorted arrays
#If it is too small or too large then there is nothing to check.
    if l1[0] + l2[0] > summ or l1[len(l1)-1] + l2[len(l2)-1] < summ:
        return 'None'
    else:
        ind = []
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] + l2[j] == summ:
                    ind.append([i,j])
                elif l1[i] + l2[j] > summ:
                    break
    return ind