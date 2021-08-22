

class DisjointSetsSystem:
    """
    Система непересекающихся множеств с произвольными данными.
    Все один в один как в обычном DisjointSet, только тут
    self.parent и self.rank - словари, где ключи - наши данные(например буквы)
    В self.parent значения(родители) будут того же типа что и ключи(тоже буквами на этом примере)
    """

    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    def make_set(self, elem):
        self.parent[elem] = elem
        self.rank[elem] = 0


    def find(self, elem):
        if elem != self.parent[elem]:
            self.parent[elem] = DisjointSetsSystem.find(self, self.parent[elem])
        return self.parent[elem]

    # при равных рангах вершина elem2 подвешивается к вершине elem1 (!)
    def union(self, elem1, elem2):
        id_1 = DisjointSetsSystem.find(self, elem1)
        id_2 = DisjointSetsSystem.find(self, elem2)
        if id_1 == id_2:
            return
        if self.rank[id_2] > self.rank[id_1]:
            self.parent[id_1] = id_2
        else:
            self.parent[id_2] = id_1
            if self.rank[id_1] == self.rank[id_2]:
                self.rank[id_1] += 1





def test():
    a = 'A'
    b = 'B'
    c = 'C'
    d = 'D'
    e = 'E'
    f = 'F'
    # аналогия с цифрами:
    # a = 1
    # b = 2
    # c = 3
    # d = 4
    # e = 5
    # f = 6

    aa = DisjointSetsSystem()

    aa.make_set(a)
    aa.make_set(b)
    aa.make_set(c)
    aa.make_set(d)
    aa.make_set(e)
    aa.make_set(f)
    print(aa.parent)
    print(aa.rank)
    print(aa.find(d))
    print()

    aa.union(b, d)
    print(aa.parent)
    print(aa.rank)
    print(aa.find(d))
    print()

    aa.union(e, b)
    print(aa.parent)
    print(aa.rank)
    print(aa.find(e))
    print()

    aa.union(c, a)
    print(aa.parent)
    print(aa.rank)
    print(aa.find(a))
    print()

    aa.union(b, c)
    print(aa.parent)
    print(aa.rank)
    print(aa.find(a))
    print(aa.parent)
    print()

    aa.union(b, f)
    print(aa.parent)
    print(aa.rank)
    print(aa.find(f))
    print()

if __name__ == '__main__':
    test()




































































































