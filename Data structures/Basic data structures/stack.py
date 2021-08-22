"""
Модуль, описывающий структуру данных - стек
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> top()
3
>>> this_stack
[1, 2, 3]
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""

this_stack = []



def is_empty(_stack=this_stack):
    return len(_stack) == 0

def push(key, _stack=this_stack):
    _stack.append(key)

def top(_stack=this_stack):
    if is_empty(_stack):
        return 'stack is empty'
    return _stack[-1]

def pop(_stack=this_stack):
    if is_empty(_stack):
        return 'stack is empty'
    return _stack.pop()

def clear(_stack=this_stack):
    _stack.clear()





if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)




















