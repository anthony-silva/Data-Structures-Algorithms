'''
    python3
    Author: Anthony Silva

    Objective: In this problem, the goal is to add parentheses to a given arithmetic
        expression to maximize its value. Find the maximum value of an arithmetic
        expression by specifying the order of applying its arithmetic operations using
        additional parentheses.

    Input: The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛,
        with symbols 𝑠0,𝑠1,...,𝑠2𝑛. Each symbol at an even position of 𝑠 is a digit
        (that is, an integer from 0 to 9) while each symbol at an odd position is one
        of three operations from {+,-,*}.

    Output: Output the maximum possible value of the given arithmetic
        expression among different orders of applying arithmetic operations.
'''

def Eval(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(M, m, i, j, operators):
    min_value = 10000000
    max_value = -10000000
    for k in range(i, j):
        a = Eval(M[i][k], M[k + 1][j], operators[k])
        b = Eval(M[i][k], m[k + 1][j], operators[k])
        c = Eval(m[i][k], M[k + 1][j], operators[k])
        d = Eval(m[i][k], m[k + 1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def GetMaxValue(values, operators):
    n = len(values)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = values[i]
        M[i][i] = values[i]

    for s in range(0, n):
        for i in range(0, n - s):
            j = i + s
            if i != j:
                m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)

    return M[0][n - 1]


if __name__ == "__main__":
    expression = input()
    operators = []
    values = []

    for char in expression:
        if char in ['+', '-', '*']:
            operators.append(char)
        else:
            values.append(int(char))

    print(GetMaxValue(values, operators))