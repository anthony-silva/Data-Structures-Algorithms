'''
 python3
 Author: Anthony Silva

 Description: The goal in this code problem is to check whether an input sequence 
	contains a majority element.

 Input: The first line contains an integer 𝑛, the next one contains a sequence of 
	𝑛 non-negative integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1. 

 Output: Output 1 if the sequence contains an element that appears strictly more 
	than 𝑛/2 times, and 0 otherwise.
'''

def MajorityElement(values, n):
	if n == 1:
		return 1

	values = sorted(values)
	count = 1
	idx = 0
	for i in range(1, n):
		if values[idx] == values[i]:
			count += 1
			if count > n/2:
				return 1
			continue
		else:
			idx += count
			count = 1
	return 0

		
if __name__ == "__main__":
	n = int(input())
	values = [int(x) for x in input().split()]
	print(MajorityElement(values, n))
