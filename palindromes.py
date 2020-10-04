from itertools import *


def all_palindromes(alphabet, n):
    ans = []
    for word in combinations_with_replacement(alphabet+alphabet[::-1], n):
        word = ''.join(word)
        k = int(len(word) / 2)
        b = word[::-1]
        if word[0:k] == b[0:k]:
            ans.append(''.join(word))
    return '\n'.join(set(ans))


print(all_palindromes('abcd', 4))

