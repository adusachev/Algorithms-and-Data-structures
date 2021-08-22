


def print_path(stack, start):
    """
    Если мы дошли до вершины start, печатает вершины, которые находятся в стеке
    """
    if stack[-1][0] == start:
        for elem in stack:
            print(elem[0], end=' ')
        print()



def reveal_all_paths(path, start, finish, stack):
    """
    Алгоритм:
    - Рабаотает рекурсивно.
    - Идем по всем возможным соседям и кладем их в стек;
      в стеке помечаю, было ли в данной вершине ветвление или нет.
    - Если мы дошли до конца, то печатаем весь пройденный путь,
      а затем удаляем все вершины из стека до начала ближайшего ветвления.
    - В какой то момент мы выведем все возможные пути, которые дает нам
      ближайшее ветвление, тогда его нужно удалить из стека.
    :param path: ориентированный граф
    :return: все пути из start в finish(для этого нужно инвертировать)
    """
    vertex = finish
    # изначально помечаю вершину как single - без ветвления(если оно есть исправлю это потом)
    stack.append([vertex, 'single'])

    if vertex == start:
        # дошли до конца, нужно вывести путь, по которому я шел:
        print_path(stack, start)
        # удаляем из стека все вершины до начала последнего ветвления(+ пока стек не пуст):
        while stack and stack[-1][1] != 'branch':
            stack.pop()
        return

    if len(path[vertex]) > 1:
        # если у вершины больше одного соседа, то в ней начнется ветвление, помечаем это в стеке
        stack[-1][1] = 'branch'
        # делаю рекурсивный вызов для ее соседей:
        for neigh in path[vertex]:
            reveal_all_paths(path, start, neigh, stack)

        stack.pop()  # удаляем из стека вершину, которая давала нам ветвление(мы вывели для нее все пути))

    if len(path[vertex]) == 1:
        # в вершине нет ветвления, так что просто делаю рекурсивный вызов для ее единственного соседа:
        neigh = path[vertex][-1]
        reveal_all_paths(path, start, neigh, stack)



def test():
    path = {'I': ['E'],
            'E': ['D', 'F'],
            'D': ['C'],
            'C': ['B'],
            'B': ['A'],
            'A': [],
            'F': ['C', 'G'],
            'G': ['C']}
    start = 'A'
    finish = 'I'
    stack = []
    reveal_all_paths(path, start, finish, stack)



def test2():
    path = {'a': ['b', 'c'],
            'b': ['f', 'g'],
            'g': ['k', 'l'],
            'f': ['h', 'i'],
            'c': ['d', 'e', 'n'],
            'd': ['m'],
            'e': ['m'],
            'n': ['m'],
            'h': ['m'],
            'i': ['m'],
            'k': ['m'],
            'l': ['m'],
            'm': []}
    start = 'm'
    finish = 'a'
    stack = []
    reveal_all_paths(path, start, finish, stack)


def test3():
    path = {'a': ['b', 'c', 'd', 'e', 'f', 'g', 'h'],
            'b': ['i'],
            'c': ['i'],
            'd': ['i'],
            'e': ['i'],
            'f': ['i'],
            'g': ['i'],
            'h': ['i'],
            'i': []}
    start = 'i'
    finish = 'a'
    stack = []
    reveal_all_paths(path, start, finish, stack)



def test4():
    path = {'a': ['b'], 'b': []}
    start = 'b'
    finish = 'a'
    stack = []
    reveal_all_paths(path, start, finish, stack)


if __name__ == '__main__':
    test2()















