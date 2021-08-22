


def graph_is_cycled(G):
    """Проверка графа на цикличность"""
    gray = set()
    black = set()
    cyclicity = [False]

    def step(vertex):
        if vertex in black:
            return
        elif vertex in gray:
            cyclicity.append(True)
            # print(vertex)
            return
        else:
            gray.add(vertex)
            for neighbour in G[vertex]:
                step(neighbour)
            black.add(vertex)

    for vertex in G:
        step(vertex)
        if cyclicity[-1]:
            return True
    return False




def test1():
    n = 5
    G = {'2': {'3'}, '1': {'5', '3', '2'}, '3': set(), '5': set()}
    print(graph_is_cycled(G))

def test2():
    n = 6
    G = {'2': {'5'}, '1': {'2'}, '3': {'2'}, '4': {'2', '6'}, '5': set(), '6': {'5'}}
    print(graph_is_cycled(G))

def test3():
    n = 6
    G = {'2': {'3'}, '1': {'2'}, '3': {'4'}, '4': {'5'}, '6': {'3'}, '5': {'6'}}
    print(graph_is_cycled(G))




if __name__ == '__main__':
    test3()
















































