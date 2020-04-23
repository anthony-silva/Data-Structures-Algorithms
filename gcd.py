'''
 python3
 Author: Anthony Silva

 Description: Implement the Euclidean algorithm for calculating the gcd 
	      of 2 numbers 
 Input: The input consists of two integers
 Output: the gcd between both integers in input
'''


def gcd(a, b):
	if b == 0:
		return a
	a = a % b
	return gcd(b, a)

if __name__ == "__main__":
	values = [int(x) for x in input().split()]
	print(gcd(values[0], values[1]))
	
