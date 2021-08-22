
from MinHeap_class import MinHeap


def build_heap(a: list):
    n = len(a)
    a = MinHeap(a)
    for i in range(n//2, -1, -1):
        a.sift_down(i)
    print(a.heap)



def test():
    a = [42, 22, 53, 18, 20, 21, 7, 18, 4]
    build_heap(a)


if __name__ == '__main__':
    test()












