# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 08:42:39 2014

@author: raffaelerainone
"""

from operator import itemgetter

#The idea is to store in a new array the couples (i,j-i+1) where i,j represents,
#respectively, the starting and lasting point of any increasing subsequence
#(hence i-j+1 represents the length of the longest increasing sequence
#that starts at i).Then we sort this array with respect to the second coordinate
#of each pair. The disadvantage is that we use some memory more
#than the necessary; however, in this way, we find all the longest increasing
#subsequences (there may be more than one, e.g. [1,2,0,1]). 
def find_it(list):
    start = 0
    B=[]
    for j in range(len(list)):
        if j == len(list)-1:
            B.append([ start, j-start+1 ])
        else:
            if list[j] >= list[j+1]:
                B.append([ start, j-start+1 ])
                start = j+1
    B=sorted(B, key = itemgetter(1))
    if len(B) > 1:
        check = True
#The following loop cancels the elements of B whose second coordinate
#are smaller than the second coordinate of B[len(B)-1] (which is the length
#of one of the longest increasing subsequence in our list)
        while check:
            if B[0][1] != B[len(B)-1][1]:
                B.pop(0)
            else:
                check = False #When we reach the element of B whose second coordinate is largest we stop the loop.
#Now we return all the longest increasing subsequence(s) in our list
#We use the slice notation for the array: if A=[0,1,2,3,4,5,6] then A[2:5] = [2,3,4].
    print [list[B[i][0]:B[i][0]+B[i][1]] for i in range(len(B))]

#Example   
#find_it([1,2,3,1,2,3,0,1])