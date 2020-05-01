'''
 Python3
 Author: Anthony Silva

 Objective: In this program I will convert an array of integers into a heap. This will be done
  by applying a certain number of swaps to the array. Swap is an operation which exchanges
  elements a_i and a_j of the array a for some i and j. The array must be converted to a heap
  in only O(n) swaps. Min-heap will be used instead of max-heap in this problem.

 Input: The first line of the input contains single integer 𝑛. The next line contains 𝑛
  space-separated integers 𝑎𝑖.

 Output: The first line of the output should contain single integer 𝑚 — the total
  number of swaps. 𝑚 must satisfy conditions 0 ≤ 𝑚 ≤ 4𝑛. The next 𝑚 lines should contain
  the swap operations used to convert the array 𝑎 into a heap. Each swap is described by a
  pair of integers 𝑖,𝑗 — the 0-based indices of the elements to be swapped. After applying
  all the swaps in the specified order the array must become a heap, that is, for each 𝑖 where
  0 ≤ 𝑖 ≤ 𝑛 − 1 the following conditions must be true:

    1. If 2𝑖+1 ≤ 𝑛−1,then 𝑎𝑖 < 𝑎2𝑖+1.
    2. If 2𝑖+2 ≤ 𝑛−1,then 𝑎𝑖 < 𝑎2𝑖+2.

  Note that all the elements of the input array are distinct.
  Note that any sequence of swaps that has length at most 4𝑛 and after which your initial
  array becomes a correct heap will be graded as correct.
'''


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [-1]
        self._data += [int(x) for x in input().split()]
        assert n == len(self._data) - 1

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def SiftDown(self, i):
        min_i = i
        left = 2 * i
        right = 2 * i + 1

        if (left <= len(self._data)-1) and (self._data[left] < self._data[min_i]):
            min_i = left
        if (right <= len(self._data)-1) and (self._data[right] < self._data[min_i]):
            min_i = right

        if i != min_i:
            self._swaps.append((i - 1, min_i - 1))
            self._data[i], self._data[min_i] = self._data[min_i], self._data[i]
            self.SiftDown(min_i)

    def GenerateSwaps(self):
        for i in range((len(self._data) - 1) // 2, 0, -1):
            self.SiftDown(i)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__=="__main__":
    heap_builder = HeapBuilder()
    heap_builder.Solve()