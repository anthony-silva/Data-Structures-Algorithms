'''
 python3
 Author: Anthony Silva

 Description: The goal in this problem is to find the minimum number of coins 
	needed to change the input value (an integer) into coins with denominations 
	1, 5, and 10.

 Input: The input consists of a single integer m
 
 Output: Output the minimum number of coins with denominations 1, 5, and 10 that changes m

 Contraints: 1 <= m <= 10^3
'''

def get_change(m):
	num_of_coins = 0
	while m != 0:
		if m-10 >= 0:
			m -= 10
		elif m-5 >= 0:
			m -= 5
		else:
			m -= 1
		num_of_coins += 1

	return num_of_coins	

if __name__ == "__main__":
	m = int(input())
	print(get_change(m))
