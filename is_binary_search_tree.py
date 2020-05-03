'''
 Python3
 Author: Anthony Silva

 Objective: You are given a binary tree with integers as its keys. You need to test whether
    it is a correct binary search tree. The definition of the binary search tree is the following:
    for any node of the tree, if its key is 𝑥, then for any node in its left subtree its key must
    be strictly less than 𝑥, and for any node in its right subtree its key must be strictly greater
    than 𝑥. In other words, smaller elements are to the left, and bigger elements are to the right.
    You need to check whether the given binary tree structure satisfies this condition. You are
    guaranteed that the input contains a valid binary tree. That is, it is a tree, and each node
    has at most two children.

 Input: The first line contains the number of vertices 𝑛. The vertices of the tree are numbered from
    0 to 𝑛−1. Vertex 0 is the root.
    The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛 − 1 in order. Each of these lines
    contains three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔h𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index
    of the left child of the 𝑖-th vertex, and 𝑟𝑖𝑔h𝑡𝑖 is the index of the right child of the 𝑖-th vertex.
    If 𝑖 doesn’t have left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔h𝑡𝑖 (or both) will be
    equal to −1.

 Output: If the given binary tree is a correct binary search tree (see the definition in the problem
    description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT”
    (without quotes).
'''

import sys, threading
sys.setrecursionlimit(2**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(j, mn, mx):
    if not j in tree:
        return True
    if tree[j][0] < mn or tree[j][0] > mx:
        return False
    return IsBinarySearchTree(tree[j][1], mn, tree[j][0]-1) and IsBinarySearchTree(tree[j][2], tree[j][0], mx)

def main():
    n = int(input())
    global tree
    tree, int_max, int_min = {}, 2**31-1, -(2**31)
    for i in range(n):
        tree[i] = [int(x) for x in input().split()]
    if IsBinarySearchTree(0, int_min, int_max):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()