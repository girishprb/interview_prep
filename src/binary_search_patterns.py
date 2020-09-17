"""
Binary search patterns
1. find exact match
2. find closest match
3. find starting index|first occurrance (left bound)
4. find ending index|last occurrance (right bound)
5. find number of occurrences
6. unidirectional binary search
7. Find in rotated sorted array
"""

from typing import List
import unittest
import random


def binary_search(arr: List[int], k: int) -> bool:
    """
    :param arr: Sorted list of integers
    :param k: key
    :return: Bool search result
    """

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == k:
            return True
        elif arr[mid] < k:
            left = mid + 1 #search in the right half
        else:
            right = mid - 1 #mid > key| Search in left half
    return False #Did not find, return False


def bs_closest_match(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid
        else:
            right = mid

    # print(arr, k, left, right, arr[left], arr[right])
    return arr[left] if abs(arr[left] - k) < abs(arr[right] - k) else arr[right]


def bs_leftmost_idx(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left+1 < right:
        mid = left + (right - left) // 2
        if arr[mid] < k:
            left = mid
        else:
            right = mid

    # print(arr, k, left, right, arr[left], arr[right])
    if arr[left] == k: return left
    if arr[right] == k: return right
    return -1


def bs_rightmost_idx(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if arr[mid] <= k:
            left = mid
        else:
            right = mid

    # print(arr, k, left, right, arr[left], arr[right])
    # print(left, arr[left], k)
    if arr[left] == k: return left
    if arr[right] == k: return right
    return -1


def bs_unidirectional(arr: List[int], k: int) -> bool:
    pw = 0
    idx = 0
    while idx < len(arr):
        if arr[idx] == k:
            return True
        elif arr[idx] > k:
            if pw > 0:
                prev_idx = pow(2, pw-1)
                print(f"searching {k} in {arr[prev_idx:idx]}")
                return binary_search(arr[prev_idx:idx], k)
            else:
                return False
        else:
            pw += 1
            idx = pow(2, pw)
    return False


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_exact_search(self):
        arr = [random.randint(0, 1000) for _ in range(100)]
        arr.sort()
        for i in range(100):
            k = random.randint(0, 1000)
            if k in arr:
                assert binary_search(arr, k)
                assert bs_unidirectional(arr, k)
            else:
                assert not binary_search(arr, k)
                assert not bs_unidirectional(arr, k)


    def test_bs_closest_match_1(self):
        arr = [0, 1, 5, 6, 7]
        assert bs_closest_match(arr, 0) == 0
        assert bs_closest_match(arr, 7) == 7
        assert bs_closest_match(arr, 4) == 5
        assert bs_closest_match(arr, 2) == 1

    def test_bs_closest_match_2(self):
        arr = [0, 10, 20, 30, 40]
        assert bs_closest_match(arr, 0) == 0
        assert bs_closest_match(arr, 11) == 10
        assert bs_closest_match(arr, 24) == 20
        assert bs_closest_match(arr, 38) == 40

    def test_bs_closest_match_3(self):
        arr = [0, 10, 20, 30, 30, 30, 30, 40]
        assert bs_closest_match(arr, 0) == 0
        assert bs_closest_match(arr, 11) == 10
        assert bs_closest_match(arr, 24) == 20
        assert bs_closest_match(arr, 38) == 40
        assert bs_closest_match(arr, 33) == 30
        assert bs_closest_match(arr, 28) == 30

    def test_bs_leftmost_idx(self):
        arr = [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 7]
        assert bs_leftmost_idx(arr, 1) == 0
        assert bs_leftmost_idx(arr, 7) == len(arr) - 1
        assert bs_leftmost_idx(arr, 4) == 3
        assert bs_leftmost_idx(arr, 5) == 7

    def test_bs_rightmost_idx(self):
        arr = [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 7]
        assert bs_rightmost_idx(arr, 1) == 0
        assert bs_rightmost_idx(arr, 7) == len(arr) - 1
        assert bs_rightmost_idx(arr, 4) == 6
        assert bs_rightmost_idx(arr, 5) == len(arr) - 2


if __name__ == '__main__':
    unittest.main()
