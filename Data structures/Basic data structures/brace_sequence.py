


import stack


def check_braces(seq: str):
    """
    :param seq: Строка, состоящая из скобок '{}[]()'
    :return: True, если данная скобочная последовательность корректна,
             False - в противном случае
    """
    for brace in seq:
        assert brace in '()[]{}'
        if brace in '([{':
            stack.push(brace)
        else:
            assert brace in ')]}'
            if stack.is_empty():
                return False
            top = stack.pop()
            if (top == '[' and brace != ']') or (top == '(' and brace != ')') \
                    or (top == '{' and brace !='}'):
                return False

    return stack.is_empty()


def main():
    seq = input()
    print(check_braces(seq))


if __name__ == '__main__':
    main()

















