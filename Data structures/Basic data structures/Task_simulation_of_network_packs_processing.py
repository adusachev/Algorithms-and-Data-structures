
class Stack:
    def __init__(self):
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def push(self, key):
        self._stack.append(key)

    def pop(self):
        if self.is_empty():
            return 'error: stack is empty'
        return self._stack.pop()

    def top(self):
        if self.is_empty():
            return 'error: stack is empty'
        return self._stack[-1]

    def clear(self):
        self._stack.clear()


# очередь:
class Queue:

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def is_empty(self):
        return bool(self.stack_in.is_empty() * self.stack_out.is_empty())

    def push_back(self, key):
        self.stack_in.push(key)

    def pop_front(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                x = self.stack_in.pop()
                self.stack_out.push(x)
        return self.stack_out.pop()






def func(size, clock):

    queue = Queue()

    if len(clock) == 0:  # если нет пакетов
        return
    free_place = size  # сколько места свободно в буфере
    processing = False  # True если идет обработка
    start = clock[0][0]  # время начала обработки
    end = clock[0][0]  # время конца обработки

    for i in range(len(clock)):

        arrival = clock[i][0]
        # блок, отвечающий за конец обработки
        if arrival >= end and i != 0:  # нужно исключить самую первую итерацию
            start = end
            processing = False
            free_place += 1

        # блок который решает класть пакет в буфер или отбросить
        if free_place != 0:
            queue.push_back(clock[i])
            free_place -= 1
        elif free_place == 0:
            queue.push_back((-1, 0))  # тоже кладу в буфер чтобы не сломался порядок вывода ответа

        # блок, отвечающий за начало обработки
        if not processing:
            x = queue.pop_front()
            while x == (-1, 0):
                print(-1)  # вывожу отброшенные
                x = queue.pop_front()
            start = max(start, x[0])  # если след пакет в буфере прибывает позже чем заканчивает обрабатываться текущий
            duration = x[1]
            end = start + duration
            print(start)
            processing = True

    # это для пакетов которые после первого цикла остались в буфере
    while not queue.is_empty():
        start = end
        x = queue.pop_front()
        if x == (-1, 0):
            print(-1)
            continue
        duration = x[1]
        start = max(start, x[0])
        end = start + duration
        print(start)







def main():
    size, n = map(int, input().split())

    clock = []
    while n != 0:
        arrival, duration = map(int, input().split())
        clock.append((arrival, duration))
        n -= 1
    func(size, clock)



def test():
    size = 1
    n = 2
    clock = [(0, 1),
             (1, 1)]
    func(size, clock)

def test2():
    size = 1
    n = 1
    clock = [(0, 0)]
    func(size, clock)


def test_my():
    size = 3
    n = 6
    clock = [(0, 7),
             (3, 4),
             (9, 5),
             (15, 2)]
    func(size, clock)

def test5():
    size = 3
    clock = [(1, 7),
             (1, 3),
             (2, 4),
             (8, 5)]
    func(size, clock)


def test6():
    size = 1
    clock = [(0, 1),
             (0, 1)]
    func(size, clock)



def test10():
    size = 1
    clock = [(999999, 1),
             (1000000, 0),
             (1000000, 1),
             (1000000, 0),
             (1000000, 0)]
    func(size, clock)

def test11():
    size = 2
    clock = [(0, 0),
             (0, 0),
             (0, 0),
             (1, 0),
             (1, 0),
             (1, 1),
             (1, 2),
             (1, 3)]
    func(size, clock)


def test12():
    size = 2
    clock = [(1, 2),
             (1, 3),
             (1, 4)]
    func(size, clock)


def test13():
    size = 2
    clock = [(0, 2),
             (0, 0),
             (2, 0),
             (3, 0),
             (4, 0),
             (5, 0)]
    func(size, clock)



if __name__ == '__main__':
    test11()






