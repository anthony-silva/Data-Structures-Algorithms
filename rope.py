'''
    Python3
    Author: Anthony Silva

    Objective: You are given a string 𝑆 and you have to process 𝑛 queries. Each query is described
        by three integers 𝑖, 𝑗, 𝑘 and means to cut substring 𝑆[𝑖..𝑗] (𝑖 and 𝑗 are 0-based) from the
        string and then insert it after the 𝑘-th symbol of the remaining string (if the symbols are
        numbered from 1). If 𝑘 = 0, 𝑆[𝑖..𝑗] is inserted in the beginning

    Input: The first line contains the initial string 𝑆.
        The second line contains the number of queries 𝑞.
        Next 𝑞 lines contain triples of integers 𝑖, 𝑗, 𝑘.

    Output: Output the string after all 𝑞 queries.
'''

class Rope:
	def __init__(self, s):
		self.s = s

	def result(self):
		return self.s

	def process(self, i, j, k):
		substring = self.s[i:j + 1]
		self.s = self.s[:i] + self.s[j + 1:]
		if k == 0:
			self.s = substring + self.s
		else:
			self.s = self.s[:k] + substring + self.s[k:]

if __name__=="__main__":
    rope = Rope(input())
    q = int(input())
    for _ in range(q):
        i, j, k = map(int, input().split())
        rope.process(i, j, k)
    print(rope.result())