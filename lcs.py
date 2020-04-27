'''
    python3
    Author: Anthony Silva

    Objective: Given two sequences 𝐴 = (𝑎1,𝑎2,...,𝑎𝑛) and 𝐵 = (𝑏1,𝑏2,...,𝑏𝑚),
        find the length of their longest common subsequence, i.e., the largest
        non-negative integer 𝑝 such that there exist indices 1 ≤ 𝑖1 < 𝑖2 <···< 𝑖𝑝 ≤ 𝑛
        and 1 ≤ 𝑗1 < 𝑗2 <···< 𝑗𝑝 ≤ 𝑚,such that 𝑎𝑖1 = 𝑏𝑗1, ... ,𝑎𝑖𝑝 = 𝑏𝑗𝑝.

    Input: First line: 𝑛
           Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛
           Third line: 𝑚
           Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚

    Output: Output p.
'''


def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first string is empty, set to 0
            if i == 0:
                dp[i][j] = 0

            # If second string is empty, set to 0
            elif j == 0:
                dp[i][j] = 0

            # If last characters are same, set to previous
            # diagonal value +1
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            # If last characters are different, set to
            # max between previous horizontal and previous
            # vertical values
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

if __name__== "__main__":
    m = int(input())
    values1 = [int(x) for x in input().split()]
    n = int(input())
    values2 = [int(x) for x in input().split()]
    print(lcs(values1, values2))