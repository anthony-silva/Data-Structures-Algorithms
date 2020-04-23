'''
 python3
 Author: Anthony Silva

 Description: Implement algorithm for calculating the least common multiple 
	      of 2 numbers 
 Input: The input consists of two integers
 Output: the lcm between both inputted integers
'''


# function for calculating gcd
def gcd(a, b):
	if b == 0:
		return a
	a = a % b
	return gcd(b, a)


# function for calculating lcm
def lcm(a, b, gcd):
	return int(a*b/gcd)


if __name__ == "__main__":
	values = [int(x) for x in input().split()]
	print(lcm(values[0],values[1],gcd(values[0], values[1])))
	
