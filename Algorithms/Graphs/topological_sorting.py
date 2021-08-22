


def Tarjan_algorithm(G):
    """Алгорит Тарьяна топологической сортировки"""
    visited = set()
    ans = []
    def dfs(start, G, visited, ans):
        visited.add(start)
        for u in G[start]:
            if u not in visited:
                dfs(u, G, visited, ans)
        ans.append(start)

    for vertex in G:
        if vertex not in visited:
            dfs(vertex, G, visited, ans)
    ans[:] = ans[::-1]
    print(ans)




def Tarjan_algorithm_2(G):
    visited = [False] * (n+1)
    ans = []
    def dfs(start, G, visited, ans):
        visited[start] = True
        for u in G[start]:
            if not visited[u]:
                dfs(u, G, visited, ans)
        ans.append(start)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, G, visited, ans)
    ans[:] = ans[::-1]
    print(ans)




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
    # print(G)
    Tarjan_algorithm(G)


def test1():
    n = 4
    G = {'B': {'C', 'D'}, 'A': {'B'}, 'C': {'D'}, 'D': set()}
    Tarjan_algorithm(G)

def test2():
    n = 6
    G = {'B': set(), 'A': {'F', 'B'}, 'C': {'B', 'D'}, 'D': set(), 'E': {'D'}, 'F': {'E'}}
    Tarjan_algorithm(G)


if __name__ == '__main__':
    test2()












































