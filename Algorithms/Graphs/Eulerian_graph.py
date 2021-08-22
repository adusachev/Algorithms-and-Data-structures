



def check_eulerianity(G):
    """
    Проверка графа на Эйлеровость:
        1) проверяю, что все степени вершин четны
        2) проверяю, что в графе только одна компонента связности
    :return: True, если граф эйлеров, False - иначе
    """
    for vertex in G:
        if len(G[vertex]) % 2 != 0:
            return False

    def dfs(vertex, G, used):
        used.add(vertex)
        for neighbour in G[vertex]:
            if neighbour not in used:
                dfs(neighbour, G, used)
    used = set()
    n = 0
    for vertex in G:
        if vertex not in used:
            dfs(vertex, G, used)
            n += 1
    if n != 1:
        return False
    return True


def find_Eulerian_cycle(G):
    """Поиск эйлерова цикла в графе"""
    degrees = {}
    for v in G:
        degrees[v] = len(G[v])
        start = v

    stack = []
    stack.append(start)
    ans = []

    while stack:
        vertex = stack[-1]
        if degrees[vertex] == 0:
            ans.append(vertex)
            stack.pop()
        else:
            neighbour = G[vertex].pop()
            G[neighbour].remove(vertex)
            stack.append(neighbour)
            degrees[vertex] -= 1
            degrees[neighbour] -= 1
    ans.pop()  # удаляем замыкание цикла
    print(*ans)




def main():
    n, m = map(int, input().split())
    G = {i: [] for i in range(1, n+1)}
    for i in range(m):
        v1, v2 = map(int, input().split())
        G[v1].append(v2)
        G[v2].append(v1)
    if check_eulerianity(G):
        find_Eulerian_cycle(G)
    else:
        print('NONE')



def test_graph():
    G = {1: {2, 3},
         2: {1, 3, 8, 7},
         3: {1, 2, 4, 5},
         4: {3, 5},
         5: {4, 3, 6, 8},
         6: {5, 8, 7, 9},
         7: {2, 8, 6, 9},
         8: {2, 5, 6, 7},
         9: {6, 7}}
    G1 = {1: {2, 3},
          2: {3, 1},
          3: {1, 2}}
    return G

def test():
    G = test_graph()
    if check_eulerianity(G):
        find_Eulerian_cycle(G)
    else:
        print('NONE')


if __name__ == '__main__':
    test()




































