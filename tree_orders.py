'''
 Python3
 Author: Anthony Silva

 Objective: In this program I will implement in-order, pre-order and post-order traversals
    of a binary tree.

 Input: The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
    from 0 to 𝑛−1. Vertex 0 is the root. The next 𝑛 lines contain information about vertices
    0, 1, ..., 𝑛 − 1 in order. Each of these lines contains three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔h𝑡𝑖 — 𝑘𝑒𝑦𝑖
    is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left child of the 𝑖-th vertex, and 𝑟𝑖𝑔h𝑡𝑖
    is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have left or right child
    (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔h𝑡𝑖 (or both) will be equal to −1.

 Output: Print three lines. The first line contains the keys of the vertices in the
    in-order traversal of the tree. The second line contains the keys of the vertices
    in the pre-order traversal of the tree. The third line contains the keys of the
    vertices in the post-order traversal of the tree.
'''

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    def traverse(node):
        if node == -1: return
        traverse(self.left[node])
        self.result.append(self.key[node])
        traverse(self.right[node])
    traverse(0)
    return self.result

  def preOrder(self):
    self.result = []
    def traverse(node):
        if node == -1: return
        self.result.append(self.key[node])
        traverse(self.left[node])
        traverse(self.right[node])
    traverse(0)
    return self.result

  def postOrder(self):
    self.result = []
    def traverse(node):
        if node == -1: return
        traverse(self.left[node])
        traverse(self.right[node])
        self.result.append(self.key[node])
    traverse(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target = main).start()