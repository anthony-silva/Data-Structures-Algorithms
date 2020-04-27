'''
    python3
    Author: Anthony Silva

    Objective: Given three sequences 𝐴 = (𝑎1,𝑎2,...,𝑎𝑛), 𝐵 = (𝑏1,𝑏2,...,𝑏𝑚), and
        𝐶 = (𝑐1,𝑐2,...,𝑐𝑙), find the length of their longest common subsequence, i.e.,
        the largest non-negative integer 𝑝 such that there exist indices
        1 ≤ 𝑖1 < 𝑖2 < ··· < 𝑖𝑝 ≤ 𝑛,
        1 ≤ 𝑗1 < 𝑗2 < ··· < 𝑗𝑝 ≤ 𝑚,
        1 ≤ 𝑘1 < 𝑘2 < ··· < 𝑘𝑝 ≤ 𝑙
        such that 𝑎𝑖1 = 𝑏𝑗1 = 𝑐𝑘1,...,𝑎𝑖𝑝 = 𝑏𝑗𝑝 = 𝑐𝑘𝑝.
        Implement dynamic programming techniques to solve the problem.

    Input: First line: 𝑛
           Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛
           Third line: 𝑚
           Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚
           Fifth line: 𝑙
           Sixth line: 𝑐1, 𝑐2, ... , 𝑐𝑙

    Output: Output 𝑝.
'''

def lcs3(str1, str2, str3):
    m = len(str1)
    n = len(str2)
    l = len(str3)

    # Create a table to store results of subproblems
    dp = [[[0 for x in range(l + 1)] for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(l + 1):
                # If first string is empty, set to 0
                if i == 0:
                    dp[i][j][k] = 0

                # If second string is empty, set to 0
                elif j == 0:
                    dp[i][j][k] = 0

                # If third string is empty, set to 0
                elif k == 0:
                    dp[i][j][k] = 0

                # If last characters are same, set to previous
                # diagonal value +1
                elif (str1[i-1] == str2[j-1]) & (str1[i-1] == str3[k-1]):
                    dp[i][j][k] = 1 + dp[i-1][j-1][k-1]

                # If last characters are different, set to
                # max previous value that is not diagonal
                else:
                    dp[i][j][k] = max(dp[i-1][j][k],
                                   dp[i][j-1][k],
                                   dp[i][j][k-1],
                                   dp[i][j-1][k-1],
                                   dp[i-1][j][k-1],
                                   dp[i-1][j-1][k],
                                   )

    return dp[m][n][k]

if __name__== "__main__":
    m = int(input())
    values1 = [int(x) for x in input().split()]
    n = int(input())
    values2 = [int(x) for x in input().split()]
    l = int(input())
    values3 = [int(x) for x in input().split()]
    print(lcs3(values1, values2, values3))