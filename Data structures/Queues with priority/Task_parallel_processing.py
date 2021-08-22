
import time

def time_test_pre():
    t_0 = time.time()
    print(str(t_0))
    return t_0


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
        while i > 0 and self.heap[MinHeap.parent(self, i)][1] >= self.heap[i][1]:
            if self.heap[MinHeap.parent(self, i)][1] == self.heap[i][1] and \
                    self.heap[MinHeap.parent(self, i)][0] < self.heap[i][0]:
                break
            else:
                self.heap[MinHeap.parent(self, i)], self.heap[i] = \
                    self.heap[i], self.heap[MinHeap.parent(self, i)]
                i = MinHeap.parent(self, i)

    def insert(self, elem: list):
        self.size += 1
        self.heap.append(elem)
        MinHeap.sift_up(self, self.size)

    def sift_down(self, i):
        min_index = i
        L = MinHeap.left_child(self, i)
        if L <= self.size and (self.heap[L][1] < self.heap[min_index][1] or
                               (self.heap[L][1] == self.heap[min_index][1] and
                                self.heap[L][0] < self.heap[min_index][0])):
            min_index = L
        # просеивается вниз, если при равных приоритетах имеет больший номер процессора
        R = MinHeap.right_child(self, i)
        if R <= self.size and (self.heap[R][1] < self.heap[min_index][1] or
                               (self.heap[R][1] == self.heap[min_index][1] and
                                self.heap[R][0] < self.heap[min_index][0])):
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
        self.heap[i][1] = float('-inf')
        MinHeap.sift_up(self, i)
        MinHeap.extract_min(self)

    def change_priority(self, i, p):
        old_p = self.heap[i][1]
        self.heap[i][1] = p
        if p < old_p:
            MinHeap.sift_up(self, i)
        else:
            MinHeap.sift_down(self, i)

    def get_min(self):
        return self.heap[0]




def build_heap(a: list):
    n = len(a)
    a = MinHeap(a)
    for i in range(n//2, -1, -1):
        a.sift_down(i)
    return a



def func(n, m, t):
    """
    Задача "Параллельная обработка"
    :param n: кол-во доступных процессоров
    :param m: кол-во задач, которые нужно обработать
    :param t: t[i] - время, необходимое на обработку i-ой задачи
    :return: Для каждой задачи: какой процессор и в какое время начнёт её обрабатывать
    """
    machines = [0] * n
    for i in range(n):
        machines[i] = [i, 0]  # machines[i] = [номер процессора, задача которую он обрабатывает]
    # Строю мин-кучу: приоритет - второе значение эл-та,
    # если приоритеты равны, приоритетным будет эл-т с меньшим номером процессора
    processing = MinHeap(machines)

    first_time = 0
    # Перебираю все m задач:
    for i in range(m):
        # Первичное обращение: заполняю кучу(здесь время начала работы у всех будет first_time = 0)
        if processing.get_min()[1] == 0:
            # сую в пустые процессоры задачи и топлю их
            processing.heap[0][1] = t[i]
            print(processing.heap[0][0], first_time)
            processing.sift_down(0)
            continue

        # Приоритеты 0 закончились:
        extracted = processing.get_min()  # "извлеченная" вершина
        time = extracted[1]

        # Ко времени "извлеченной" вершины, добавляю время следующей задачи и топлю ее:
        processing.heap[0][1] += t[i]
        print(processing.heap[0][0], time)
        processing.sift_down(0)







def main():
    n, m = map(int, input().split())
    t = list(map(int, input().split()))
    func(n, m, t)

def test():
    n = 2
    m = 5
    t = [1, 2, 3, 4, 5]
    func(n, m, t)

def test2():
    n = 4
    m = 10
    t = [7, 4, 2, 5, 8, 3, 1, 10, 9, 6]
    func(n, m, t)

def test3():
    n = 4
    m = 20
    t = [1] * m
    func(n, m, t)

def test4():
    n = 2
    m = 15
    t = [0, 0, 1, 0, 0, 0, 2, 1, 2, 3, 0, 0, 0, 2, 1]
    func(n, m, t)

def time_test():
    t_0 = time_test_pre()
    from random import randint
    n = randint(1, 10**5)
    m = randint(1, 10**5)
    t = []
    for i in range(m):
        t.append(randint(1, 10**9))

    func(n, m, t)

    t_1 = time.time()
    print(str(t_1))
    print(t_1 - t_0, 'sec')

if __name__ == '__main__':
    test3()










