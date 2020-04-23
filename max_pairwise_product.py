'''
 python3
 Author: Anthony Silva

 Description: Find the maximum product of two distinct numbers in a sequence of
	      non-negative integers.

 Input: A sequence of non-negative integers.
 Output: The max value that can be obtained by multiplying two different
	 elements from the sequence.
'''

def MaxPairwiseProduct(nums):
	if len(nums)<2:
		return -1

	max1 = nums[0]
	max1_idx = 0
	for i in range(len(nums)):
		if nums[i] > max1:
			max1 = nums[i]
			max1_idx = i
	
	max2 = 0
	for j in range(len(nums)):
		if (j != max1_idx) & (nums[j] >= max2):
			max2 = nums[j]

	return (max1 * max2)

if __name__ == "__main__":
	count = int(input())
	numbers = [int(x) for x in input().split()]
	print(MaxPairwiseProduct(numbers))
			
			
