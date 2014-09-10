# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 12:38:06 2014

@author: raffaelerainone
"""

#==============================================================================
# FIRST FUNCTION. Reverse one word.
#==============================================================================
#The following function reverses one word and it will be used in the main
#function, below.
def reverse_word(word):
    return word[::-1]
#I believe that the purpose of the exercise is to test my algorithmical ability,
#and this is the reason why I also give the following, that does the same:
#    result = []
#    for i in range(len(word)):
#        result.append(word[len(word)-i-1])
#    return "".join(result)#This commands simply makes the array into a string.

#==============================================================================
# SECOND FUNCTION. Given a string reverse each word in it.
#==============================================================================
#Now I create the function that reverses the order of the letters in each word
#of the given string.
#
#The idea is to create an array that comprises each word (and space) of the given
#string, and while we append the new word to the array we also reverse it.
#Then it is enough to transform this array in a string,
#by concatenating the elements in it, we use "".join(array)
#that simply concatenate all the elements in the array
#
#The code would be much simpler using .split()

def reverse_words_string(string):
    string = string.lower()#we make all the characters lower case
#The following index will be used in the loop below.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z','0','1','2','3','4','5','6','7','8','9']
#The first word starts at index 0, then it will start at j whenever string[j-1]=
#a space or a comma or a symbol not in the alphabet.
    start = 0
#This is the array where we will store each word reversed and the spaces.
    result = []
#This loop does the following:
#1. If j=len(string)-1. If string[j] is not a letter or a number then our string terminates as "word ".
#So to result we append the reversed word and then a space.
# If string[j] is a letter or a number then the string terminates as "word". So to result we append
#only the reversed word.
#2. If j!= len(string)-1. We check if string[j] is not in the alphabet (e.g. it is a space),
#in this case the word goes from string[start] up to string[j].
#Hence, in the array we append the reversed word string[start:j]
    for j in range(len(string)):
        if j == len(string)-1:
            if string[j] not in alphabet:
                result.append(reverse_word(string[start:j]))
                result.append(string[j])
            else:
                result.append(reverse_word(string[start:j+1]))
        else:
            if string[j] not in alphabet or j == len(string)-1:
                result.append(reverse_word(string[start:j]))
                if j!=len(string)-1:
                    result.append(string[j])
                start=j+1
#So far, we have created a list, called result, with each word reversed and spaces,
#e.g. if string="Hello, world" then result=["olleh", ",", " ", "dlrow"]
#The following simply transforms the list in a string, by concatenating
#the different elements in the string with the character "" (i.e. no character)
#between two consecutive items in the list.
    result = "".join(result)
    print result

#reverse_words_string('hello, world')