"""
Problem: https://leetcode.com/problems/longest-happy-prefix

"""

# Rolling Hash
def longestPrefix(self, s):
    res, l, r, mod = 0, 0, 0, 10 ** 9 + 7
    for i in range(len(s) - 1):
        l = (l * 128 + ord(s[i])) % mod
        r = (r + pow(128, i, mod) * ord(s[~i])) % mod
        if l == r: res = i + 1
    return s[:res]


# KMP
class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 1: return ''

        def KMPSearch(pat, txt):
            M, N = len(pat), len(txt)
            lps = failure(pat)

            i = 0  # index for txt[]
            j = 0  # index for pat[]
            while i < N:
                if pat[j] == txt[i]:
                    i += 1
                    j += 1
                elif i < N and pat[j] != txt[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
                if i >= N:
                    return i - j

        def failure(pat):
            res = [0]
            i, target = 1, 0
            while i < len(pat):
                if pat[i] == pat[target]:
                    target += 1
                    res += target,
                    i += 1
                elif target:
                    target = res[target - 1]
                else:
                    res += 0,
                    i += 1
            return res

        l = len(s) - 1 - KMPSearch(s[:-1], s[1:])
        return s[:l]