'''
 python3
 Author: Anthony Silva

 Description: Your friend is making a text editor for programmers. He is currently
    working on a feature that will find errors in the usage of different types of
    brackets. Code can contain any brackets from the set []{}(), where the opening
    brackets are [,{, and ( and the closing brackets corresponding to them are ],}, and ).
    For convenience, the text editor should not only inform the user that there is an
    error in the usage of brackets, but also point to the exact place in the code with
    the problematic bracket. First priority is to find the first unmatched closing bracket
    which either doesn’t have an opening bracket before it, like ] in ](), or closes the
    wrong opening bracket, like } in ()[}. If there are no such mistakes, then it should
    find the first unmatched opening bracket without the corresponding closing bracket
    after it, like ( in {}([]. If there are no mistakes, text editor should inform the user
    that the usage of brackets is correct.

    Apart from the brackets, code can contain big and small latin letters, digits and
    punctuation marks.

    More formally, all brackets in the code should be divided into pairs of matching
    brackets, such that in each pair the opening bracket goes before the closing bracket,
    and for any two pairs of brackets either one of them is nested inside another one as
    in (foo[bar]) or they are separate as in f(a,b)-g[c]. The bracket
    [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).


 Input: Input contains one string 𝑆 which consists of big and small latin letters, digits,
    punctuation marks and brackets from the set []{}().


 Output: If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes).
    Otherwise, output the 1-based index of the first unmatched closing bracket, and if there
    are no unmatched closing brackets, output the 1-based index of the first unmatched opening
    bracket.
'''

def CheckBrackets(text):
    stack = [] # stack for storing open brackets
    idx = [] # stack for storing indexes of open brackets

    for i in range(len(text)):
        if text[i] in ['[', '{', '(']:
            stack.append(text[i])
            idx.append(i)
        elif (text[i] in [']', '}', ')']) and (len(stack) == 0):
            return i
        elif text[i] == ']':
            top = stack.pop()
            if top != '[':
                return i
            idx.pop()
        elif text[i] == '}':
            top = stack.pop()
            if top != '{':
                return i
            idx.pop()
        elif text[i] == ')':
            top = stack.pop()
            if top != '(':
                return i
            idx.pop()
        else:
            continue

    if len(stack) == 0: # if stack is empty then Success
        return 'Success'
    else: # else return index of last unmatched bracket
        return idx.pop()


if __name__ == "__main__":
    print(CheckBrackets(input()))
