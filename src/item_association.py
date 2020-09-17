import collections
import unittest


def tie_breaker(l1, l2):
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            continue
        else:
            return l1 if l1[i] < l2[i] else l2

    return l1


class UnionFind(object):
    def __init__(self):
        self.id = {}
        self.num_components = 0
        self.comp_size = collections.Counter()

    def join(self, item1, item2):
        p1 = self.find(item1)
        p2 = self.find(item2)
        # if common root, nothing to join
        if p1 == p2:
            return

        # pick the smaller one and merge to the larger one
        if self.comp_size[p1] <= self.comp_size[p2]:
            self.comp_size[p2] += self.comp_size[p1]
            self.id[p1] = p2
            del self.comp_size[p1]
        else:
            self.comp_size[p1] += self.comp_size[p2]
            self.id[p2] = p1
            del self.comp_size[p2]

        # print(f"joining {item1} and {item2}")
        # print(self.id, self.comp_size)
        self.num_components -= 1

    def find(self, item):
        # create a new component if it does not exist
        if item not in self.id:
            self.id[item] = item
            self.comp_size[item] = 1
            self.num_components += 1
            return item

        # Traverse the parents to find the root
        parent = self.id[item]
        while self.id[parent] != parent:
            parent = self.id[parent]

        # Path compression
        while item != parent:
            next = self.id[item]
            self.id[item] = parent
            item = next

        return parent

    def max_component(self):
        res_map = collections.defaultdict(list)
        for k, v in self.id.items():
            res_map[v].append(k)

        res = []
        for k, v in res_map.items():
            v.sort()
            if len(v) > len(res):
                res = v
            elif len(v) == len(res):
                res = tie_breaker(v, res)

        return res


def items_association_uf(items_list):
    uf = UnionFind()
    for items in items_list:
        uf.join(items[0], items[1])

    return uf.max_component()


def items_association_dfs(items_list):
    """
    Input: list of lists: [[i1, i2], [i2, i3], [i4,i5],[i8,i8]]
    Output: [i1, i2, i3]
    """

    graph = collections.defaultdict(set)

    for items in items_list:
        graph[items[0]].add(items[1])
        graph[items[1]].add(items[0])

    visited = set()
    res = []

    for n in graph.keys():
        if n in visited:
            continue
        stack = [n]
        tmp_res = []
        while stack:
            i = stack.pop()
            tmp_res.append(i)
            for j in graph[i]:
                if j not in visited:
                    stack.append(j)
            visited.add(i)

        tmp_res.sort()
        if len(tmp_res) > len(res):
            res = tmp_res
        elif len(tmp_res) == len(res):
            res = tie_breaker(res, tmp_res)
    return res


class TestItemAssociation(unittest.TestCase):
    def test1(self):
        ip = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['e', 'f']]
        res = items_association_dfs(ip)
        print(res)
        assert res == ['a', 'b', 'c', 'd']

    def test2(self):
        ip = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['e', 'f']]
        res = items_association_uf(ip)
        print(res)
        assert res == ['a', 'b', 'c', 'd']


if __name__ == '__main__':
    unittest.main()
