'''
 python3
 Author: Anthony Silva

 Objective: The edit distance between two strings is the minimum number of operations
    (insertions, deletions, and substitutions of symbols) to transform one string into
    another. It is a measure of similarity of two strings. This program computes the
    edit distance between two strings using Dynamic Programming.

 Input: Each of the two lines of the input contains a string consisting of lower case latin
    letters.

 Output: The edit distance between the given two strings.
'''


def EditDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    if m == 0:
        return n # return the length of str2
    if n == 0:
        return m # return the length of str1

	# Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	# Fill d[][] in bottom up manner
    for i in range(m + 1):
	    for j in range(n + 1):

			# If first string is empty, only option is to
			# insert all characters of second string
		    if i == 0:
			    dp[i][j] = j # Min. operations = j

			# If second string is empty, only option is to
			# remove all characters of second string
		    elif j == 0:
			    dp[i][j] = i # Min. operations = i

			# If last characters are same, ignore last char
			# and recur for remaining string
		    elif str1[i-1] == str2[j-1]:
			    dp[i][j] = dp[i-1][j-1]

			# If last characters are different, consider all
			# possibilities and find minimum
		    else:
			    dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
								dp[i-1][j],	 # Remove
								dp[i-1][j-1]) # Replace
    return dp[m][n]

if __name__== "__main__":
    print(EditDistance(input(), input()))