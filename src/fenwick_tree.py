class FenwickTree:
    """
    Cumulative frequency Table for values in range [0,n]
    Space complexity: O(n)
    Range Sum Query: O(log n)
    Handling updates: O(log n)

    Best suited for: dynamic Range Sum Queries on discrete arrays
    """
    def __init__(self, n):
        self.ft = [0] * (n+1)
        self.n = n+1

    @staticmethod
    def __LSOne(i):
        # Return least significant bit
        return i & (-i)

    def rsq(self, i):
        total = 0
        while i:
            total += self.ft[i]
            i -= FenwickTree.__LSOne(i)

        return total

    def rsq_range(self, i , j):
        return self.rsq(j) - (self.rsq(i-1) if i > 1 else 0)

    def adjust(self, k, v):
        while k < self.n:
            self.ft[k] += v
            k += self.__LSOne(k)

from typing import List
"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/submissions/
"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        rank = {val: i + 1 for i, val in enumerate(sorted(nums))}
        print(rank)

        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            update(rank[x])
            print(f'updating {rank[x]}: {BITree}')
            res.append(getSum(rank[x] - 1))

        print(BITree)
        return res[::-1]

import unittest

class TestFenwickTree(unittest.TestCase):
    def test1(self):
        arr = [2, 4, 5, 5, 6, 6, 6, 7, 7, 8, 9]
        ft = FenwickTree(10)

        for a in arr:
            ft.adjust(a, 1)

        assert ft.rsq(1) == 0
        assert ft.rsq(5) == 4
        assert ft.rsq(7) == 9
        assert ft.rsq(10) == 11

    def test2(self):
        arr = [2, 4, 5, 5, 6, 6, 6, 7, 7, 8, 9]
        ft = FenwickTree(10)

        for a in arr:
            ft.adjust(a, 1)

        assert ft.rsq_range(1,4) == 2
        assert ft.rsq_range(5, 6) == 5
        assert ft.rsq_range(7, 9) == 4
        assert ft.rsq_range(8, 9) == 2


if __name__ == '__main__':
    unittest.main()

