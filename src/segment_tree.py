

class SegmentTree:
    """
    Implementing segment tree using binary heap
    for Range Minimum Query
    Left Tree: (2 * i) + 1
    Right Tree: (2 * i) + 2
    Index of the Parent: (i-1) // 2
    TODO:
        1. handling updates to existing array
        2. handling adds/dels to existing array
    """

    def __init__(self, arr):
        self.arr = arr
        st_size = self.get_st_size()
        self.st = [float('inf')] * st_size
        self.construct_st(0, len(arr)-1, 0)

    def get_st_size(self):
        multiplier = 1
        n = len(self.arr)

        while multiplier < n:
            multiplier *= 2

        return 2 * multiplier - 1

    def construct_st(self, low, high, pos):
        if low == high:
            self.st[pos] = self.arr[low]
        else:
            mid = (low + high) // 2
            left_st_idx = SegmentTree.__left(pos)
            right_st_idx = SegmentTree.__right(pos)
            self.construct_st(low, mid, left_st_idx)
            self.construct_st(mid + 1, high, right_st_idx)
            self.st[pos] = min(self.st[left_st_idx], self.st[right_st_idx])

    def __rmq(self, pos, L, R, i, j):
        #print(pos, L, R, i, j)
        if i > R or j < L:
            return float('inf')
        if L >= i and R <= j:
            #print(pos, L, R, i, j)
            return self.st[pos]
        mid = (L + R) // 2
        p1 = self.__rmq(SegmentTree.__left(pos), L, mid, i, j)
        p2 = self.__rmq(SegmentTree.__right(pos), mid+1, R, i, j)

        return min(p1, p2)

    @staticmethod
    def __left(p):
        return (2 * p) + 1

    @staticmethod
    def __right(p):
        return (2 * p) + 2

    def rmq(self, i, j):
        return self.__rmq(0, 0, len(self.arr)-1, i, j)


import unittest


class TestSegmentTree(unittest.TestCase):
    def test1(self):
        arr = [5, 3, 1, 7, 3, 9, 0]
        st = SegmentTree(arr)
        print(st.st)

    def test1(self):
        arr = [5, 3, 1, 7, 3, 9, 0]
        st = SegmentTree(arr)
        assert st.rmq(0, 0) == 5
        assert st.rmq(1, 2) == 1
        assert st.rmq(3, 5) == 3
        assert st.rmq(5, 6) == 0
        assert st.rmq(0, 6) == 0


if __name__ == '__main__':
    unittest.main()



