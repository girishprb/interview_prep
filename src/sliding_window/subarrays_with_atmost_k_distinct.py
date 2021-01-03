"""
sliding window patterns: https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235002/One-code-template-to-solve-all-of-these-problems!
"""

import collections


def subarrays_with_at_most_k_distinct(self, s, k):
    lookup = collections.defaultdict(int)
    l, r, counter, res = 0, 0, 0, 0

    while r < len(s):
        lookup[s[r]] += 1
        if lookup[s[r]] == 1:
            counter += 1
        r += 1
        while l < r and counter > k:
            lookup[s[l]] -= 1
            if lookup[s[l]] == 0:
                counter -= 1
            l += 1
        res += r - l

    return res