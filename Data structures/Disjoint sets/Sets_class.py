

class DisjointSet:
    """
    Класс система непересекающихся множеств
    """

    def __init__(self):
        self.parent = []
        self.rank = []

    def make_set(self, i):
        while len(self.parent) - 1 < i:
            self.parent.append(0)
            self.rank.append(0)
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = DisjointSet.find(self, self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = DisjointSet.find(self, i)
        j_id = DisjointSet.find(self, j)
        if i_id == j_id:
            return
        if self.rank[j_id] > self.rank[i_id]:
            self.parent[i_id] = j_id
        else:
            self.parent[j_id] = i_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[i_id] += 1





def test():
    a = DisjointSet()

    a.make_set(1)
    a.make_set(2)
    a.make_set(3)
    a.make_set(4)
    a.make_set(5)
    a.make_set(6)
    print(a.parent)
    print(a.rank)
    print(a.find(4))
    print()

    a.union(2, 4)
    print(a.parent)
    print(a.rank)
    print(a.find(4))
    print()

    a.union(5, 2)
    print(a.parent)
    print(a.rank)
    print(a.find(5))
    print()

    a.union(3, 1)
    print(a.parent)
    print(a.rank)
    print(a.find(1))
    print()

    a.union(2, 3)
    print(a.parent)
    print(a.rank)
    print(a.find(1))
    print(a.parent)
    print()

    a.union(2, 6)
    print(a.parent)
    print(a.rank)
    print(a.find(6))
    print()


def test2():
    a = DisjointSet()

    a.make_set(1)
    a.make_set(2)
    a.make_set(3)
    a.make_set(4)
    a.make_set(5)
    a.make_set(6)
    a.make_set(7)
    a.make_set(8)
    a.make_set(9)
    a.make_set(10)
    a.make_set(11)
    a.make_set(12)
    print(a.parent)
    print(a.rank)
    print()

    a.union(10, 5)
    a.union(7, 10)
    a.union(3, 5)
    a.union(2, 3)
    a.union(12, 3)
    a.union(8, 12)
    a.union(6, 12)
    a.union(11, 6)
    a.union(1, 6)
    a.union(9, 5)
    a.union(4, 9)
    print(a.parent)
    print(a.rank)
    print()

    a.make_set(0)
    print(a.parent)
    print(a.rank)
    print()



if __name__ == '__main__':
    test()


