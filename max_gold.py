'''
    python3
    Author: Anthony Silva

    Objective: You are given a set of bars of gold and your goal is
        to take as much gold as possible into your bag. There is just
        one copy of each bar and for each bar you can either take it or not
        (hence you cannot take a fraction of a bar). Given 𝑛 gold bars, find
        the maximum weight of gold that fits into a bag of capacity 𝑊 .

    Input: The first line of the input contains the capacity 𝑊 of a knapsack
        and the number 𝑛 of bars of gold. The next line contains 𝑛 integers
        𝑤0 , 𝑤1 , . . . , 𝑤𝑛−1 defining the weights of the bars of gold.

    Output: Output the maximum weight of gold that fits into a knapsack of capacity 𝑊
'''

def OptimalWeight(W, w):
    dp = [[0 for x in range(W + 1)] for x in range(len(w) + 1)]

    for i in range(0, len(w) + 1):
        for j in range(0, W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif w[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(w[i - 1] + dp[i - 1]
                [j - w[i - 1]], dp[i - 1][j])

    return dp[len(w)][W]


if __name__== "__main__":
    weight = [int(x) for x in input().split()]
    max_weight = weight[0]
    n = weight[1]
    weights = [int(x) for x in input().split()]
    print(OptimalWeight(max_weight, weights))