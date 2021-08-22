

_stack = []

def is_empty():
    return len(_stack) == 0

def push(key):
    _stack.append(key)

def top():
    if is_empty():
        return 'stack is empty'
    return _stack[-1]

def pop():
    if is_empty():
        return 'stack is empty'
    return _stack.pop()

def clear():
    _stack.clear()




def check_braces(seq: str):
    """
    :param seq: Строка, состоящая из заглавных и прописных букв латинского
                алфавита, цифр, знаков препинания и скобок из множества []{}()

    :return: Если скобки в seq расставлены правильно, выводит строку “Success".
             В противном случае выводит индекс (используя индексацию с единицы)
             первой закрывающей скобки, для которой нет соответствующей открывающей.
             Если такой нет, выводит индекс первой открывающей скобки,
             для которой нет соответствующей закрывающей
    """
    k = 0
    for brace in seq:
        k += 1
        if brace in '()[]{}':
            if brace in '([{':
                push((brace, k))  # поддерживаю номера открывающихся скобок

            else:
                assert brace in ')]}'
                if is_empty():
                    print(k)
                    return
                top = pop()[0]
                if (top == '[' and brace != ']') or (top == '(' and brace != ')') \
                        or (top == '{' and brace !='}'):
                    print(k)
                    return

    if is_empty():
        print('Success')
    else:
        print(pop()[1])



def main():
    line = input()
    check_braces(line)

main()




















