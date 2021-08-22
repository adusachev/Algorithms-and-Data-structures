"""
Структура данных - стек с поддержкой минимума
>>> push(2)
>>> get_min()
2
>>> push(4)
>>> get_min()
2
>>> push(1)
>>> get_min()
1
>>> push(3)
>>> get_min()
1
>>> push(5)
>>> get_min()
1
>>> min_list
[2, 2, 1, 1, 1]
>>> this_stack
[2, 4, 1, 3, 5]
"""

this_stack = []
min_list = []

def is_empty(_stack=this_stack):
    return len(_stack) == 0

def push(key, _stack=this_stack, mins=min_list):
    _stack.append(key)
    if is_empty(mins) or key <= top(mins):
        mins.append(key)
    else:
        mins.append(top(mins))

def top(_stack=this_stack):
    if is_empty(_stack):
        return 'stack is empty'
    return _stack[-1]

def pop(_stack=this_stack, mins=min_list):
    if is_empty(_stack):
        return 'stack is empty'
    mins.pop()
    return _stack.pop()

def clear(_stack=this_stack, mins=min_list):
    _stack.clear()
    mins.clear()

def get_min(mins=min_list):
    return top(mins)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)








