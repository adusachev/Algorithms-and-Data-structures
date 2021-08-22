


class MaxHeap:

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
        while i > 0 and self.heap[MaxHeap.parent(self, i)] < self.heap[i]:
            self.heap[MaxHeap.parent(self, i)], self.heap[i] = \
                self.heap[i], self.heap[MaxHeap.parent(self, i)]
            i = MaxHeap.parent(self, i)

    def insert(self, p):
        self.size += 1
        self.heap.append(p)
        MaxHeap.sift_up(self, self.size)

    def sift_down(self, i):
        max_index = i
        L = MaxHeap.left_child(self, i)
        if L <= self.size and self.heap[L] > self.heap[max_index]:
            max_index = L
        R = MaxHeap.right_child(self, i)
        if R <= self.size and self.heap[R] > self.heap[max_index]:
            max_index = R
        # max_index - индекс наибольшего эл-та из вершины i и ее детей
        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            MaxHeap.sift_down(self, max_index)

    def extract_max(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        MaxHeap.sift_down(self, 0)
        return result

    def remove(self, i):
        self.heap[i] = float('inf')
        MaxHeap.sift_up(self, i)
        MaxHeap.extract_max(self)

    def change_priority(self, i, p):
        old_p = self.heap[i]
        self.heap[i] = p
        if p > old_p:
            MaxHeap.sift_up(self, i)
        else:
            MaxHeap.sift_down(self, i)


a = MaxHeap([42, 29, 18, 14, 7, 16, 12, 11, 5])
print(a.heap)
print(a.size)








































