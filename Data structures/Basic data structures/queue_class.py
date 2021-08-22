"""
Cтруктура данных - очередь(наследована от класса стек)
>>> q = Queue()
>>> q.stack_in._stack
[]
>>> q.stack_out._stack
[]
>>> q.is_empty()
True
>>> q.push_back(1)
>>> q.push_back(2)
>>> q.push_back(3)
>>> q.push_back(4)
>>> q.stack_in._stack
[1, 2, 3, 4]
>>> q.stack_out._stack
[]
>>> q.pop_front()
1
>>> q.stack_in._stack
[]
>>> q.stack_out._stack
[4, 3, 2]
>>> q.push_back(5)
>>> q.stack_in._stack
[5]
>>> q.stack_out._stack
[4, 3, 2]
>>> q.pop_front()
2
>>> q.stack_in._stack
[5]
>>> q.stack_out._stack
[4, 3]
>>> q.is_empty()
False
"""

from stack_class import Stack


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

























