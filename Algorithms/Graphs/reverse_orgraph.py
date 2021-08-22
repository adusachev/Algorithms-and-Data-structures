


def reverse_graph(G):
    """
    :param G: исходный ориентированный граф
    :return: граф G1 с противоположной ориентацией
    Вроде правильно(по моим примерам)
    """
    G1 = {}
    for vertex in G:
        for neighbour in G[vertex]:
            if neighbour not in G1:
                G1[neighbour] = {vertex}
            else:
                G1[neighbour].add(vertex)
    for vertex in G:
        if vertex not in G1:
            G1[vertex] = set()
    print(G1)





def main():
    n, m = [int(x) for x in input().split()]
    G = {}
    for i in range(m):
        v1, v2 = input().split()
        if v2 not in G:
            G[v2] = set()
        if v1 not in G:
            G[v1] = {v2}
        else:
            G[v1].add(v2)
    print(G)


def test1():
    n = 5
    G = {'2': {'3'}, '1': {'5', '3', '2'}, '3': set(), '5': set()}
    reverse_graph(G)

def test2():
    n = 6
    G = {'2': {'5'}, '1': {'2'}, '3': {'2'}, '4': {'2', '6'}, '5': set(), '6': {'5'}}
    reverse_graph(G)

def test3():
    n = 6
    G = {'2': {'3'}, '1': {'2'}, '3': {'4'}, '4': {'5'}, '6': {'3'}, '5': {'6'}}
    reverse_graph(G)


if __name__ == '__main__':
    test3()






























