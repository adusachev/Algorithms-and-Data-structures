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


def matrix_mult_bottom_up(sizes: list):
    """
    :param sizes: размеры матриц (для [50, 20, 1, 10, 100] - А(50x20), B(20x1), C(1x10), D(10x100))
    :return: минимальная стоимость умножения всех матриц
    """
    n = len(sizes) - 1          # кол-во мартиц на 1 меньше кол-ва размеров
    d = [[float('inf') for j in range(n)] for i in range(n)]
    for i in range(n):
        d[i][i] = 0

    ans = {}  # для восстановления ответа
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            min_value = d[i][j]  # для восстановления ответа
            for k in range(i, j):
                d[i][j] = min(d[i][j], d[i][k] + d[k+1][j] + sizes[i]*sizes[k+1]*sizes[j+1])

                if d[i][j] < min_value:
                    min_value = d[i][j]
                    k1 = k    # запоминаем значение k, на котором реализовался минимум данной ячейки
            ans[(i, j)] = k1   # получим словарь вида: ключ - с какой по какую матрицу нужно перемножить, значение - индекс где нужно поставить "пробел"

    get_table(d, 3)

    def get_mult_order(ans: dict, i, j):
        """
        начальные: i = 0, j = n - 1, дальше рекурсивно
        выводит порядок индексов, которыми нужно разбить порядок умножения(см примеры и ответы)
        """
        if i == j:
            return
        space = ans[(i, j)]
        print(space)
        next1 = (i, space)  # первый интервал от разбиения числом space
        next2 = (space+1, j)  # второй интервал от разбиения числом space
        get_mult_order(ans, next1[0], next1[1])
        get_mult_order(ans, next2[0], next2[1])

    print('optimal multiplication order:')
    get_mult_order(ans, 0, n-1)
    print('min cost of multiplication:')
    return d[0][n-1]



def test():
    # ответ: ((А0 х А1) х (А2 х А3))
    sizes = [50, 20, 1, 10, 100]
    print(matrix_mult_bottom_up(sizes))

def test2():
    # ответ:  ((A0 x (A1 x A2)) x ((A3 x A4) x A5))
    sizes = [30, 35, 15, 5, 10, 20, 25]
    print(matrix_mult_bottom_up(sizes))

def test3():
    # ответ: ((A0 x (A1 x A2)) x A3)
    sizes = [10, 29, 133, 8, 15]
    print(matrix_mult_bottom_up(sizes))

def test4():
    # ответ:  (((((A0 x A1) x A2) x A3) x (A4 x A5)) x A6)
    sizes = [1, 5, 28, 19, 2, 10, 1, 12]
    print(matrix_mult_bottom_up(sizes))


if __name__ == '__main__':
    test()




















































