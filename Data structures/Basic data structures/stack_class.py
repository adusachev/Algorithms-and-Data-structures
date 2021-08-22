"""
Модуль, описывающий структуру данных - стек (через классы)
>>> a.clear()
>>> a.is_empty()
True
>>> a.push(1)
>>> a.push(2)
>>> a.push(3)
>>> a.is_empty()
False
>>> a.top()
3
>>> a._stack
[1, 2, 3]
>>> a.pop()
3
>>> a.pop()
2
>>> a.pop()
1
>>> a.is_empty()
True
"""


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




a = Stack()



























