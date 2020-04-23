'''
 python3
 Author: Anthony Silva

 Objective: To force the given implementation of the quick sort algorithm to efficiently 
	process sequences with few unique elements, the goal is replace a 2-way partition 
	with a 3-way partition. That is, the new partition procedure should partition the 
	array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.

 Input: The first line of the input contains an integer 𝑛. The next line contains a sequence 
	of 𝑛 integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

 Output: Output this sequence sorted in non-decreasing order 
'''


import random


def Partition(values, l, r):
	pivot, j, k = values[l], l, r
	i = j
	while i <= k:
		if values[i] < pivot:
			values[i], values[j] = values[j], values[i] # swap values
			j += 1 # shift index in left partition one right
		elif values[i] > pivot:
			values[i], values[k] = values[k], values[i] # swap values
			k -= 1 # shift index in right partition one left
			i -= 1 # keep i in place
		i += 1
	return j, k # return first index and last index of middle partition with equal values to pivot


def RandomizedQuickSort(values, l, r):
	if l >= r: # case solution found
		return True

	k = random.randint(l,r) # select random index from subarray
	values[l], values[k] = values[k], values[l] # swap left most value in array and random value
	m1, m2 = Partition(values, l, r) # get equal values in their final position and return index
	RandomizedQuickSort(values, l, m1-1) # sort left partition subarray
	RandomizedQuickSort(values, m2+1, r) # sort right partition subarray

		
if __name__ == "__main__":
	n = int(input()) # total number of values in original array
	values = [int(x) for x in input().split()] # elements in original array
	RandomizedQuickSort(values, 0, n-1) # run randomized quicksort3 on values
	
	# print solution
	for x in values:
		print(x, end=' ')
