def get_table(a: str, b: str, d: list, sep_num=1):
    """выводит таблицу для наглядности"""
    # для удобства можно транспонировать таблицу(см файл "рюкзак без повторений")
    print('------------')
    print(a)
    print(b)
    m = len(d)
    n = len(d[0])
    for k in range(n):
        print(' '*sep_num, k, end='')
    print()
    for p in range(m):
        print(p, d[p])
    print()



def diff(a: str, b: str):
    if a == b:
        return 0
    return 1

def edit_dist_bottom_up(a: str, b: str):
    """вычисляет расстояние редактирования строк а и b"""
    n = len(a)
    m = len(b)
    d = [[float('inf') for j in range(m+1)] for i in range(n+1)]
    # get_table(a, b, d, 3)
    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1):
        d[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            c = diff(a[i-1], b[j-1])  # индексы у самих строк, поэтому они на единичку меньше
            Ins = d[i-1][j] + 1
            Del = d[i][j-1] + 1
            Sub = d[i-1][j-1] + c
            d[i][j] = min(Ins, Del, Sub)
    get_table(a, b, d)
    return d[n][m]



def main():
    a = input()
    b = input()
    print(edit_dist_bottom_up(a, b))

def test():
    assert edit_dist_bottom_up('short', 'ports') == 3
    assert edit_dist_bottom_up('ab', 'ba') == 2
    assert edit_dist_bottom_up('editing', 'distance') == 5
    assert edit_dist_bottom_up('ab', 'ab') == 0
    print(edit_dist_bottom_up('editing', 'distance'))

if __name__ == '__main__':
    test()
























































