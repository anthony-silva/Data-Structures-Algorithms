'''
 python3
 Author: Anthony Silva

 Description: The goal in this code problem is to implement the binary search algorithm.

 Input: The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 
	of 𝑛 pairwise distinct positive integers in increasing order. The next line contains an 
	integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
 
 Output: For all 𝑖 from 0 to 𝑘−1, output an index 0 ≤ 𝑗 ≤ 𝑛−1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there
	is no such index.

 Contraints: 1 ≤ 𝑘 ≤ 105; 1 ≤ 𝑛 ≤ 3·104; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 109 for all
	0 ≤ 𝑗 < 𝑘
'''

import numpy as np

def BinarySearch(values, left, right, key):
	if right < left:
		return -1

	mid = int(left + ((right-left)/2))

	if key == values[mid]:
		return mid
	elif key < values[mid]:
		return BinarySearch(values, left, mid-1, key)
	else:
		return BinarySearch(values, mid+1, right, key)	
		
		
if __name__ == "__main__":
	values1 = [int(x) for x in input().split()]
	values2 = [int(x) for x in input().split()]
	n1 = values1.pop(0) # number of elements in first list
	n2 = values2.pop(0) # number of elements in second list
	results = [0] * n2

	for i in range(n2):
		results[i] = BinarySearch(values1, 0, len(values1)-1, values2[i])

	print(" ".join(map(str, results)))
