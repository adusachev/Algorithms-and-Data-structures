


from decimal import Decimal, ROUND_FLOOR




def func(x: Decimal, coefs: list):
    """
    :param x: некоторая точка
    :param coefs: коэффициенты многочлена
    :return: значение многочлена в точке x
    """
    assert type(x) is Decimal, 'Проверьте тип х'
    assert type(coefs[0]) is Decimal, 'Проверьте типы коэффициентов'  # проверю первый для примера
    x_deg = []  # будет список [x**n, x**(n-1), ..., x]
    x_i = 1
    for i in range(len(coefs) - 1):
        x_i *= x  # вычисляю степени числа x
        x_deg.append(x_i)
    # список нужно развернуть, чтобы потом поставить ему в соответствие список коэффициентов:
    x_deg.reverse()
    ans = Decimal('0')
    for j in range(len(x_deg)):
        ans += (x_deg[j] * coefs[j])
    # не забываем про свободный член coefs[-1]
    return ans + coefs[-1]



def find_L_R(coefs):
    """
    Вычисление интервала (L, R), в котором может находиться корень.
    (так как неизвестно, какая именно функция подастся на вход)
    :return: (L, R)
    """
    from random import randint
    L = Decimal('2')
    R = Decimal('1')
    f_L = Decimal('1')
    f_R = Decimal('1')
    while f_L * f_R >= 0 or R < L:
        L = Decimal(str(randint(-100, 100)))
        R = Decimal(str(randint(-100, 100)))
        f_L = func(L, coefs)
        f_R = func(R, coefs)
    print('L = ' + str(L) + '; ' + 'f(' + str(L) + ') = ' + str(func(L, coefs)))
    print('R = ' + str(R) + '; ' + 'f(' + str(R) + ') = ' + str(func(R, coefs)))
    return L, R



def find_root(coefs, delta=0.000000001):
    """
    Поиск корня уравнения нек действительнозначной
    непрерывной монотонной(!) функции.
    (в данном случае функция это многочлен)
    :param coefs: коэффициенты многочлена
    :param delta: точность определения корня
    :return: корень уравнения
    """
    L_R = find_L_R(coefs)
    L = L_R[0]
    R = L_R[1]
    # сам алгоритм:
    while R - L > delta:
        middle = (L + R) / 2
        if func(middle, coefs) < 0.0:
            L = middle
        else:
            R = middle
    root = (L + R) / 2

    return root





def main():
    print('Степень многочлена:')
    n = int(input())
    print('Коэффициенты(в порядке от х**n до x**0):')
    coefs = list(map(float, input().split()))
    assert len(coefs) == n + 1, 'Указанное число коэффициентов не соответствует степени многочлена'
    for i in range(n + 1):
        coefs[i] = Decimal(str(coefs[i]))
    print(find_root(coefs))

    

def test():
    n = 5
    coefs = [1, 0, 7, 0, 3, -8]
    for i in range(n + 1):
        coefs[i] = Decimal(str(coefs[i]))
    print(find_root(coefs))


def test2():
    n = 5
    coefs = [16, 0, 7.99, 2.5, -3, -8]
    for i in range(n + 1):
        coefs[i] = Decimal(str(coefs[i]))
    print(find_root(coefs))


def test3():
    n = 5
    coefs = [42, -20, -38, -38, 2, -38]
    for i in range(n + 1):
        coefs[i] = Decimal(str(coefs[i]))
    print(find_root(coefs))




if __name__ == '__main__':
    main()









