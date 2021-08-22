

class MinHeap:

    def __init__(self, h=[]):
        self.heap = h
        self.size = len(h) - 1

    def parent(self, i):
        return (i-1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_up(self, i):
        while i > 0 and self.heap[MinHeap.parent(self, i)] > self.heap[i]:
            self.heap[MinHeap.parent(self, i)], self.heap[i] = \
                self.heap[i], self.heap[MinHeap.parent(self, i)]
            i = MinHeap.parent(self, i)

    def insert(self, p):
        self.size += 1
        self.heap.append(p)
        MinHeap.sift_up(self, self.size)

    def sift_down(self, i):
        min_index = i
        L = MinHeap.left_child(self, i)
        if L <= self.size and self.heap[L] < self.heap[min_index]:
            min_index = L
        R = MinHeap.right_child(self, i)
        if R <= self.size and self.heap[R] < self.heap[min_index]:
            min_index = R
        # min_index - индекс наименьшего эл-та из вершины i и ее детей
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            MinHeap.sift_down(self, min_index)

    def extract_min(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        MinHeap.sift_down(self, 0)
        return result

    def remove(self, i):
        self.heap[i] = float('-inf')
        MinHeap.sift_up(self, i)
        MinHeap.extract_min(self)

    def change_priority(self, i, p):
        old_p = self.heap[i]
        self.heap[i] = p
        if p < old_p:
            MinHeap.sift_up(self, i)
        else:
            MinHeap.sift_down(self, i)

    def get_min(self):
        return self.heap[0]


b = MinHeap([4, 18, 7, 20, 21, 18, 42, 53, 22])

print(b.heap)
print(b.size)
#
# b.remove(8)
# print(b.heap)
print(b.get_min())
print(b.heap)







