# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 16:14:31 2014

@author: raffaelerainone
"""
#==============================================================================
# INTRODUCTION
#==============================================================================
#The main problem is: How do we store a binary search tree?
#
#EXAMPLE0: Let us consider the following tree:
#      A
#   /    \
#  B     C
# /     / \
#D     E   F
#     /
#    G
#
#DEFINITION. A binary search tree is a binary tree where each node has an assigned 
#value (a number) with some restrictions: e.g. v(B)<v(A)<v(C), etc.
#
#DEFINITION: A binary search tree is balanced if and only if
#the underlying tree is balanced. (Below I discuss the balanced property.)
#
#Therefore, to solve our problem, we only need the tree as input (we do not
#need the value of each node).
#Again, the question is: How do we store a Binary (search) tree?
#
#(METHOD I). I would do the following: tree = [node,[left_subtree],[right_subtree]]
#For Example0: tree_1 = [A,[B,[[D,[],[]],[]]],[C,[E,[[G],[]]],[F,[],[]]]].
#This way may probably be useful for certain type of problems; however,
#for our purpose, it is not a good way.
#
#(METHOD II).
#DEFINITION. THE COMPLETE binary tree is the binary tree where each nodes has
#exactly two branches exit from it. (It is infinite.)
#(Equivalently it is the binary tree whose level n contains exactly 2^{n-1} nodes).
#FACT: Each binary tree is contained in the complete binary tree.
#
#We can enumerate the nodes of the complete binary tree in a natural way:
#         1
#       /   \
#      2     3
#     / \   / \
#    4  5  6  7
#  etc.
#We translate these numbers to binary and then to string: '1', '10', '11', etc.
#The input for the complete binary tree will be the infinite string ['1','10',...].
#
#Essentially, the root is labelled '1'. Then any new node inherits the label
#from its previous one and we add '0' or '1' at the end, '0' if the new node is
#on the right and '1' if it is on the left.
#
#To identify a given binary tree, we only need to know the labels
#of its node.
#
#Therefore the INPUT, for EXAMPLE0 above is:
# tree = ['1','10','11','100','110','111','1100']
#
#We will use Method II from this point on.
#==============================================================================

#==============================================================================
# FIRST FUNCTION. "Compute height".
#==============================================================================

#The following function computes the height of a node.
#As input we give the (binary) string that identifies the node and the tree.
#Recall that by definition, if the node is not in the tree then its height is -1.
#In case the node belongs to the given tree then its height, by definition,
#is the longest path from the node to a leaf. In particular, leaves have
#height equal to 0.
#
#In the following we take a node from the tree and we compute its height.
#
#The idea of how to compute the height of a node that belongs to the given tree
#is explained with the aid of the following, EXAMPLE1 (that is Example0
#translated in the notation of Method II):
#      1
#    /   \
#   10   11
#  /    /  \
#100  110  111
#     /
#   1100
#The height of 11 is 2 (this is clear by the picture and the above definition).
#A way to compute its height is to check the longest chain of string inclusion(*): 
#{(*) DEFINITION: Given two strings X,Y we say that X is an L-substring of Y
#(this stays for Left-substring), and we write XcY if Y[0:len(X)]=X}.
#For example, 'home'c'homeland' but 'home' is not an L-substring of 'hhome'.
#With this definition in mind we have (in the tree of EXAMPLE1):
# '11'c'110'c'1100' AND '11'c'111', and '11' is not an L-substring of any other
#string in the tree. Thus the height is the LONGEST chain of inclusion.
#Therefore the height of '11' is two.
#
#But we know also that the length of a string (of a node) represents the level
#where that node belongs. For example, '11' is on the second level.
#Therefore, to compute the height of '11' we need to know the maximum of
#len(STRING) - len('11') for any STRING that satisfies the following two properties:
#(1). len(STRING) > len('11').
#(2). '11'c STRING --> that means: STRING[0:len('11')] = '11'.
#After this explanation the following function should be clear (as input we
#need the tree because if the given node does not belong to the tree then
#its height is -1).

def compute_h(node,tree):
    if node not in tree:
        height = -1
    else:
        l = len(node)
        height = 0
#The next loop goes through all the nodes in the tree and does several checks,
#IF the tree is ordered, e.g. instead of tree = ['1','10,'100','11']
#we must give as input tree = ['1','10,'11','100'] then we can avoid to check
#among all the nodes and we can start from the given node.(This will increase the efficiency.)
        for new_node in tree:
            if len(new_node) > l and new_node[0:l] == node and len(new_node)-l > height:
                height = len(new_node) - l
    return height

#==============================================================================
# SECOND FUNCTION. "The nearest node to a node".
#==============================================================================
#First we give two definitions:
#DEFINITION. We say that a node A in a tree is THE parent of the node B
#if A is in level i, B is in level i+1 and there is a branch that connects A and B.
#In the above example '11' is the parent of '110' (and of '111')
#but it is not the parent of '1100'.
#
#DEFINITION. Given a tree and two nodes A and B in it, we say that A is
#the nearest node to B (and so B is the nearest node to A) if and only if they
#have the same parent. We will also say that A and B are nearest nodes.
#
#With our presentation of a tree it is clear that if we take a node A
#(assume its last character is 0) then the nearest node to A is given
#by the string A[0:len(A)-1]+'1'.
#For example, the nearest node of '11001' is '11000'. (If a node is in the given
#tree then it is not true in general that its nearest node belongs to the tree
#as well, e.g.'1100' in EXAMPLE1)
#
#With this example in mind the following construction of the nearest node is clear.
#Given a node A, we return new_node, which is the nearest node to A.

def nearest_node(node):
    l = len(node)
    new_node = node[0:l-1]
    if node[l-1] == '1':
        new_node +='0'
    else:
        new_node += '1'
    return new_node


#==============================================================================
#FINAL FUNCTION. "Check if a tree is balanced".
#==============================================================================
#
#A tree is balanced if and only if all the differences of the heights
#of two nearest nodes is either -1 or 0 or 1.
#
#We start checking the differences of heights of elements from the bottom
#of the tree, and we stop the first time we find a difference >1 or <-1.
#
#The idea of starting from the bottom arise from the intuition that if a tree is
#not balanced then some differences in the bottom should not verify the condition
#of being -1,0, or 1. However, we can have a tree:
#   1
# /  \
#10  massive balanced subtrees
#
#Then the algorithm for this tree takes long time to run.
#However, in the same way we can have a massive tree, that terminates with a subtree
#that is not balanced. Again, if we start from the top, the algorithm for
#this case will be inefficient.
#
#The Input is a tree, given in the form explained in the Section INTRODUCTION
#the Output is True or False, depending whether or not the tree is balanced.

def is_balanced(tree):
    i=0 #This is the index used in the while loop.
    l = len(tree) #we store the number of nodes in our tree for convenience.
    final_check = True #this tells us if the tree is balanced or not.
    while final_check and i<l-1:
        node1 = tree[l-i-1] #we store the first node and we shall compute its nearest one.
        if node1[len(node1)-1] == 0: #in the case node1 is on the left, and its nearest node (say node2)
        #is in the tree then we have already computed h(node1)=h(node2) in the previous step.
            if nearest_node(node1) not in tree:
                if compute_h(node1,tree)+1 not in [-1,0,1]:
                    final_check = False
        else:
            node2 = nearest_node(node1)
            if compute_h(node1,tree) - compute_h(node2,tree) not in [-1,0,1]:
                final_check = False
        i += 1
    print final_check
'''
tree1 = ['1','10','11','100','110','111','1100']#this is balanced
tree2 = ['1','10','11','110','1100']#this is NOT balanced
tree3 = ['1','10','11','100','110','1100']#this is NOT balanced
tree4 = ['1','10','11','100','110','1100','111']#this is balanced
tree5 = ['1','10','11','110','111','1111']#this is NOT balanced

is_balanced(tree1)
is_balanced(tree2)
is_balanced(tree3)
is_balanced(tree4)
is_balanced(tree5)
'''
