import unittest


def string_compare(s, t, i, j):
    """
    Brute force recursive approach
    - branch 3 ways: (same, insert, delete)
    - O(3^n)
    """
    if i == 0:
        return j
    if j == 0:
        return i

    if s[i] == t[j]:
        return string_compare(s, t, i-1, j-1)

    return 1 + min(string_compare(s, t, i-1, j),    #Remove
                   string_compare(s, t, i, j-1),    #insert
                   string_compare(s, t, i-1, j-1))  #Replace


def edit_distance_dp(s, t, m, n):
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

    return dp[m][n]


class TestEditDistance(unittest.TestCase):
    def test_brute_force(self):
        res = string_compare("abcd", "abcc", 3, 3)
        self.assertEqual(res, 1)
        res = string_compare("abcdefgh", "abcc", 7, 3)
        self.assertEqual(res, 5)

    def test_dp(self):
        res = edit_distance_dp("abcd", "abcc", 3, 3)
        self.assertEqual(res, 1)
        res = edit_distance_dp("abcdefgh", "abcc", 7, 3)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()