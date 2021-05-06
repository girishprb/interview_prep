import functools
import unittest

class HashTable:
    def __init__(self, length = 4):
        self.array = [None] * length
        self.total = 0

    def __hash__(self, key):
        return hash(key) % len(self.array)

    def set(self, key, value):
        if self.__is_full():
            self.__double()

        idx = self.__hash__(key)

        if not self.array[idx]:
            self.array[idx] = [[key, value]]
            self.total += 1
            return

        for kvp in self.array[idx]:
            if kvp[0] == key:
                kvp[1] = value
                return

        self.array[idx].append([key, value])
        self.total += 1
        return

    def get(self, key):
        idx = self.__hash__(key)
        if not self.array[idx]:
            raise KeyError()

        for kvp in self.array[idx]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError()

    def __is_full(self):
        count = sum(1 for x in self.array if x)
        return count >= len(self.array) // 2

    def __double(self):
        ht2 = HashTable(length=len(self.array) * 2)
        for a_list in self.array:
            if not a_list:
                continue

            for kvp in a_list:
                ht2.set(kvp[0], kvp[1])

        self.array = ht2.array
        self.total = ht2.total

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __len__(self):
        return self.total


class TestHashTable(unittest.TestCase):
    def test1(self):
        ht = HashTable()
        ht['abc'] = 123
        ht['xyz'] = 456
        assert ht['abc'] == 123
        assert ht['xyz'] == 456
        assert len(ht) == 2

if __name__ == '__main__':
    unittest.main()
