


def dijkstra(G, start):
    """
    Алгоритм Дейкстры.
    :param G: неориентированный взвешенный граф, веса - неортицательные числа, вершины - буквы
    :param start: нач вершина
    :return: словарь кратчайших расстояний от start до всех остальных вершин
    """
    from collections import deque
    queue = deque()
    s = dict()  # словарь кратчайших расстояний
    for vertex in G:
        s[vertex] = float('inf')
    s[start] = 0
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        for neighbour in G[vertex]:
            old_s = s[neighbour]
            edge_len = G[vertex][neighbour]
            potential_new_s = s[vertex] + edge_len
            if (neighbour not in s) or (potential_new_s < old_s):
                s[neighbour] = potential_new_s
                queue.append(neighbour)
    return s





def reveal_shortest_path(G, start, finish, shortest_distance):
    """Находит какой-то один кратчайший путь"""
    path = [finish]
    vertex = finish
    while vertex != start:
        for neighbour in G[vertex]:
            vertex_dist = shortest_distance[vertex]
            neighbour_dist = shortest_distance[neighbour]
            edge_len = G[vertex][neighbour]
            if neighbour_dist == vertex_dist - edge_len:
                optimal_neighbour = neighbour
                path.append(optimal_neighbour)
                vertex = neighbour
                break
    return path





def read_graph():
    m = int(input())  # m - кол-во ребер
    G = {}
    # далее m строк: "А Б вес"
    for i in range(m):
        a, b, weight = input().split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G

def add_edge(G, a, b, weight):
    # делаю словарь словарей смежности:
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight



def main():
    G = read_graph()
    # G = test_graph()
    start = input('Enter a start vertex: ')
    while start not in G:
        start = input('There is no such vertex in the graph.\n' +
                      'Enter a start vertex: ')

    shortest_distances = dijkstra(G, start)
    print('Shortest distances from ' + start + ' to other vertexes:')
    print(shortest_distances)

    finish = input('Enter a finish vertex: ')
    while finish not in G:
        finish = input('There is no such vertex in the graph.\n' +
                       'Enter a finish vertex: ')

    shortest_path = reveal_shortest_path(G, start, finish,
                                         shortest_distances)
    print('One of the possible shortest paths from ' + start + ' to ' + finish + ':')
    print(shortest_path)



def test_graph():
    G = {'A': {'B': 2.0, 'H': 15.0},
         'B': {'A': 2.0, 'C': 1.0, 'D': 5.0},
         'C': {'B': 1.0, 'D': 3.0, 'G': 1.0, 'F': 2.0},
         'D': {'B': 5.0, 'C': 3.0, 'F': 4.0, 'E': 6.0},
         'E': {'D': 6.0, 'F': 7.0, 'I': 2.0},
         'F': {'C': 2.0, 'D': 4.0, 'G': 1.0, 'E': 7.0, 'H': 3.0},
         'G': {'C': 1.0, 'F': 1.0},
         'H': {'A': 15.0, 'F': 3.0, 'I': 12.0},
         'I': {'H': 12.0, 'E': 2.0}}
    return G


def test():
    G = test_graph()
    start = 'A'
    finish = 'I'
    s = dijkstra(G, start)
    print('Shortest distances from ' + start + ' to other vertexes:')
    print(s)
    path = reveal_shortest_path(G, start, finish, s)
    print('One of the possible shortest paths from ' + start + ' to ' + finish + ':')
    print(path)



def test2():
    G = {'A': {'B': 1.0, 'C': 2.0},
         'B': {'A': 1.0, 'C': 1.0, 'D': 3.0},
         'C': {'A': 2.0, 'B': 1.0, 'D': 12.0},
         'D': {'B': 3.0, 'C': 12.0}}


if __name__ == '__main__':
    test()












































