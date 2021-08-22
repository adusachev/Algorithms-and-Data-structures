
def transporate_table(d: list):
    """транспонирует таблицу"""
    trans = []
    for j in range(len(d[0])):
        trans.append([])
        for i in range(len(d)):
            trans[j].append(d[i][j])
    return trans

def get_table(d: list, sep_num=1):
    """
    выводит таблицу
    sep_num - кол-во пробелов в нумерации
    """
    print('------------')
    m = len(d)
    n = len(d[0])
    for k in range(n):
        print(' '*sep_num, k, end='')
    print()
    for p in range(m):
        print(p, d[p])
    print()

def knapsack_without_reps(W: int, weights: list, costs: list):
    """
    :param W: вместимость рюкзака(целое)
    :param weights: веса предметов(целые)
    :param costs: стоимости предметов(целые)
    :return: max стоимость предметов суммарного веса не более W (без повторений предметов)
    """
    n = len(weights)
    d = [[float('inf') for i in range(n+1)] for w in range(W+1)]
    get_table(transporate_table(d), 3)
    for w in range(0, W+1):
        d[w][0] = 0
    for i in range(0, n+1):
        d[0][i] = 0
    for i in range(1, n+1):
        w_i = weights[i-1]
        c_i = costs[i-1]
        for w in range(1, W+1):
            d[w][i] = d[w][i-1]
            if w_i <= w:
                d[w][i] = max(d[w][i], d[w - w_i][i - 1] + c_i)
    get_table(transporate_table(d))
    return d[W][n]

def main():
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = weights
    print(knapsack_without_reps(W, weights, costs))

def test():
    assert knapsack_without_reps(0, [2, 4, 6], [45, 23, 67]) == 0
    assert knapsack_without_reps(5, [5], [23]) == 23
    assert knapsack_without_reps(5, [10], [34]) == 0
    print(knapsack_without_reps(10, [6, 3, 4, 2], [30, 14, 16, 9]))

if __name__ == '__main__':
    test()



















































