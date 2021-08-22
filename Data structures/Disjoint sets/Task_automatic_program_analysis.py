

from Sets_class import DisjointSet


def func(n, e, d, equal: list, inequal: list):
    numbers = DisjointSet()
    for x in equal:
        numbers.make_set(x[0])
        numbers.make_set(x[1])
    # print(numbers.parent)
    for x in equal:
        numbers.union(x[0], x[1])
    # print(numbers.parent)


    if len(numbers.parent) == 0:
        for x in inequal:
            if x[0] == x[1]:
                print(0)  # test4
                return
        print(1)  # test3
        return

    for x in inequal:
        if x[0] > len(numbers.parent) - 1 or x[1] > len(numbers.parent) - 1:
            pass
        elif numbers.find(x[0]) == numbers.find(x[1]):
            print(0)
            return
    print(1)






def main():
    n, e, d = map(int, input().split())

    e_list = []
    while e != 0:
        i, j = map(int, input().split())
        e_list.append((i, j))
        e -= 1

    d_list = []
    while d != 0:
        i, j = map(int, input().split())
        d_list.append((i, j))
        d -= 1
    func(n, e, d, e_list, d_list)



def test():
    n = 4
    e = 6
    d = 0
    equal = [(1, 2),
              (1, 3),
              (1, 4),
              (2, 3),
              (2, 4),
              (3, 4)]
    inequal = []
    func(n, e, d, equal, inequal)


def test2():
    n = 6
    e = 5
    d = 3
    equal = [(2, 3),
             (1, 5),
             (2, 5),
             (3, 4),
             (4, 2)]
    inequal = [(6, 1),
               (4, 6),
               (4, 5)]
    func(n, e, d, equal, inequal)

def test3():
    n = 1
    e = 0
    d = 1
    equal = []
    inequal = [(1, 1)]
    func(n, e, d, equal, inequal)

def test4():
    n = 4
    e = 0
    d = 6
    inequal = [(1, 2),
               (1, 3),
               (1, 4),
               (2, 3),
               (2, 4),
               (3, 4)]
    equal = []
    func(n, e, d, equal, inequal)

if __name__ == '__main__':
    test3()










































