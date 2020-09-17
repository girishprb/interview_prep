"""
Given two rectangles with (x1, y1, h, w) - left bottom
Find the intersecting rectangle in the same format

"""

def get_intersecting_rectangle(r1, r2):
    #find bottom interecting x
    def find_intersection_1d(p11, p12, p21, p22):
        res_p = -1
        res_x = -1
        if p11 <= p21 < p12:
            res_p = p21
            res_x = min(p12, p22) - p21

        elif p21 <= p11 < p22:
            res_p = p11
            res_x = min(p12, p22) - p11

        return [res_p, res_x]

    x11 = r1[0]
    x12 = r1[0] + r1[3]

    x21 = r2[0]
    x22 = r2[0] + r2[3]

    res_x, res_w = find_intersection_1d(x11, x12, x21, x22)
    if res_w == -1:
        return None

    y11 = r1[1]
    y12 = r1[1] + r1[2]

    y21 = r2[1]
    y22 = r2[1] + r2[2]

    res_y, res_h = find_intersection_1d(y11, y12, y21, y22)
    if res_h == -1:
        return None
    return [res_x, res_y, res_h, res_w]

import unittest


class TestRectangleIntersection(unittest.TestCase):

    def test1(self):
        r1 = [0, 0, 5, 5]
        r2 = [1, 1, 7, 7]
        print(get_intersecting_rectangle(r1, r2))

        r1 = [0, 0, 3, 3]
        r2 = [4, 4, 7, 7]
        print(get_intersecting_rectangle(r1, r2))

        r1 = [5, 5, 3, 3]
        r2 = [4, 4, 7, 7]
        print(get_intersecting_rectangle(r1, r2))

        r1 = [5, 5, 3, 3]
        r2 = [4, 4, 7, 7]
        print(get_intersecting_rectangle(r1, r2))


if __name__ == '__main__':
    unittest.main()


