'''
 python3
 Author: Anthony Silva

 Description: In this program I implement the Rabin–Karp’s algorithm for
    searching for a given pattern in the given text.

 Input: There are two strings in the input: the pattern 𝑃 and the text 𝑇.

 Output: Prints all the positions of the occurrences of 𝑃 in 𝑇 in the ascending order.
    Uses 0-based indexing of positions in the the text 𝑇.

 Contraints: 1 ≤ |𝑃| ≤ |𝑇| ≤ 5·10^5. The total length of all occurrences of 𝑃 in 𝑇 doesn’t exceed 10^8.
    The pattern and the text contain only latin letters
'''


def GetOccurrences(pattern, text):
    output = []
    l = len(pattern)
    hashed_value = sum([ord(pattern[i]) for i in range(len(pattern))])
    current_hashed = sum([ord(text[:l][i]) for i in range(len(text[:l]))])
    if text[:l] == pattern:
        output.append(0)
    for i in range(1, len(text) - l + 1):
        current_hashed = current_hashed - ord(text[i - 1]) + ord(text[i + l - 1])
        if current_hashed == hashed_value:
            if text[i:i + l] == pattern: output.append(i)
    return output


if __name__ == '__main__':
    print(' '.join(map(str, GetOccurrences(input(), input()))))