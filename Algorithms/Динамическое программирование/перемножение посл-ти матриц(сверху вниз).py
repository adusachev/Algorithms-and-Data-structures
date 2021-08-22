def get_table(d: list, sep_num=1):
    """
    выводит табличку(это только для наглядности)
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



d = [[float('inf') for j in range(4)] for i in range(4)]

def matrix_mult_top_down(sizes: list, i, j):
    global d
    if d[i][j] == float('inf'):
        if i == j:
            d[i][j] = 0
        else:
            for k in range(i, j):
                L = matrix_mult_top_down(sizes, i, k)
                R = matrix_mult_top_down(sizes, k+1, j)
                print(L, R)
                d[i][j] = min(d[i][j], L + R + sizes[i]*sizes[k+1]*sizes[j+1])  # в sizes увеличены индексы на 1
    get_table(d, 3)
    return d[i][j]


def test():
    sizes = [50, 20, 1, 10, 100]
    i = 0
    j = len(sizes) - 2
    print(matrix_mult_top_down(sizes, i, j))

test()




















































