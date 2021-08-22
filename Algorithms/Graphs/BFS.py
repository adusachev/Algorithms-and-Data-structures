




def bfs(G, start_vertex, n):
    """
    Обход графа в ширину.
    :param G: невзвешенный неориентированный граф(вершины - числа от 1 до n)
    :param start_vertex: начальная вершина
    :param n: кол-во вершин в графе
    :return: список distances:
             distances[i] = кратчайшее расстояние от start_vertex до i-ой вершины графа
    """
    from collections import deque
    distances = [None] * n  # список расстояний
    distances[start_vertex] = 0
    queue = deque([start_vertex])  # очередь создаем сразу с нач эл-том

    while queue:  # <=> пока очередь не пуста
        vertex = queue.popleft()
        for neighbour in G[vertex]:
            if distances[neighbour] is None:  # <=> вершина еще не посещена(расстояние до нее не вычислено)
                distances[neighbour] = distances[vertex] + 1
                queue.append(neighbour)
    print(distances)





def main():
    n, m = map(int, input().split())
    G = {i: set() for i in range(n)}
    for i in range(m):
        v1, v2 = map(int, input().split())
        G[v1].add(v2)
        G[v2].add(v1)
    print(G)
    start_vertex = int(input())
    bfs(G, start_vertex, n)


def test():
    n, m = 15, 16
    G = {0: {1, 10, 11, 12},
         1: {0, 7},
         2: {6},
         3: {11},
         4: {10},
         5: {8, 13},
         6: {2, 10},
         7: {1, 13},
         8: {12, 5},
         9: {11},
         10: {0, 4, 6},
         11: {0, 3, 9, 12, 14},
         12: {0, 8, 11},
         13: {5, 7},
         14: {11}}
    start_vertex = 0
    bfs(G, start_vertex, n)


if __name__ == '__main__':
    test()































