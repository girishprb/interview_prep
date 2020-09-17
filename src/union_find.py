from typing import List


class UnionFind(object):
    def __init__(self):
        self.union_map = {}
        self.intervals = {}

    def exists(self, v):
        return v in self.union_map

    def add(self, v):
        assert v not in self.union_map
        self.union_map[v] = v
        self.intervals[v] = [v, v]

    def find(self, v):
        if v not in self.union_map:
            return None

        if self.union_map[v] != v:
            self.union_map[v] = self.find(self.union_map[v])
        # print(f'parent of {v} is {self.union_map[v]}')
        return self.union_map[v]

    def union(self, v1, v2):
        # print(f'union for {v1}, {v2}')
        p1 = self.find(v1)
        p2 = self.find(v2)

        # print(p1, p2)
        if p1 is None or p2 is None:
            return

        if p1 == p2:
            return

        p1_interval = self.intervals[p1]
        del self.intervals[p1]

        self.union_map[p1] = p2

        self.intervals[p2] = [min(p1_interval[0], self.intervals[p2][0]), max(p1_interval[1], self.intervals[p2][1])]

        # print(self.union_map, self.intervals)


class SummaryRanges:

    def __init__(self):
        self.uf = UnionFind()

    def add_num(self, val: int) -> None:
        if self.uf.exists(val):
            return

        self.uf.add(val)
        self.uf.union(val, val - 1)
        self.uf.union(val, val + 1)

    def get_intervals(self) -> List[List[int]]:
        return sorted(self.uf.intervals.values(), key=lambda x: (x[0], x[1]))


import unittest


class TestSummaryRanges(unittest.TestCase):
    def test1(self):
        sr = SummaryRanges()
        for i in [1,3,5,7,9,2]:
            sr.add_num(i)

        print(sr.get_intervals())
        sr.add_num(4)
        print(sr.get_intervals())

if __name__ == '__main__':
    unittest.main()


"""
Alternate implementation:
"""


class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m

        n, ans = len(arr), -1
        uf = UnionFindSet(n)

        for step, i in enumerate(arr):
            i -= 1
            uf.ranks[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j]:
                        uf.union(i, j)

        return ans