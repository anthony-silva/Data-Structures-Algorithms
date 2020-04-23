'''
 python3
 Author: Anthony Silva

 Description: Given an integer n, find the last digit of
	      the nth Fibonacci number F(n)

 Input: The input consists of a single integer n

 Output: Last digit of the nth Fibonacci number

 Contraints: 0 <= n <= 45
'''

import numpy as np

def LastFibonacci(n):
	if n <= 1:
		return n

	seq = np.zeros(n)
	seq[0], seq[1] = 1, 1
	for i in range(2, n):
		seq[i] = (seq[i-1] + seq[i-2]) % 10
	return int(seq[n-1])

if __name__ == "__main__":
	n = int(input())
	print(LastFibonacci(n))
	
