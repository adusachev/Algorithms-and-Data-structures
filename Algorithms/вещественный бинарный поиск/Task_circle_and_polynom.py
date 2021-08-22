
"""
Дана окружность, многочлен и точка X. Гарантируется, что (x, f(x))
лежит внутри окружности. Найти пересечение многочлена с окружностью.

В единственной строке выведите xx координату точки, в которой многочлен пересекает окружность.
Если таких точек несколько, выведите любую.
"""


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
    x_deg.reverse()
    ans = Decimal('0')
    for j in range(len(x_deg)):
        ans += (x_deg[j] * coefs[j])
    # не забываем про свободный член coefs[-1]
    return ans + coefs[-1]




def find_L_R(x, coefs, circle):
    """
    Вычисление интервала (L, R), в котором может находиться корень.
    (здесь L и R будут точки с координатами)
    :return: (L, R)
    """
    L = (x, func(x, coefs))
    y_c = circle[1]
    x_c = circle[2] + circle[0]
    R = (x_c, y_c)
    return L, R




\def find_root(coefs, circle, x, delta=0.00000000001):
    """
    :param coefs: коэффициенты многочлена
    :param circle: Параметры окружности(x_c, y_c, r)
    :param x: Точка х, такая что (x, f(x)) лежит внутри окружности
    :param delta: точность определения корня
    :return: координата х точки пересечения многочлена с окружностью(одной из двух)
    """
    x_c = circle[0]
    y_c = circle[1]
    r = circle[2]
    L_R = find_L_R(x, coefs, circle)
    L = L_R[0]
    R = L_R[1]
    L = L[0]
    R = R[0]
    while R - L > delta:
        middle = (L + R) / 2
        x_o = middle
        y_o = func(middle, coefs)
        if (x_o - x_c)**2 + (y_o - y_c)**2 < r**2:
            L = middle
        else:
            R = middle
    root = (L + R) / 2

    return root




def main():
    print('Параметры окружности(x_c, y_c, r):')
    circle = list(map(float, input().split()))
    assert len(circle) == 3, 'Ошибка ввода'
    for i in range(3):
        circle[i] = Decimal(str(circle[i]))
    print('Степень многочлена:')
    n = int(input())
    print('Коэффициенты(в порядке от х**n до x**0):')
    coefs = list(map(float, input().split()))
    assert len(coefs) == n + 1, 'Указанное число коэффициентов не соответствует степени многочлена'
    for i in range(n + 1):
        coefs[i] = Decimal(str(coefs[i]))
    print('Точка х, такая что (x, f(x)) лежит внутри окружности:')
    x = float(input())
    x = Decimal(str(x))
    # print(find_L_R(x, coefs, circle))
    print(find_root(coefs, circle, x))




def test():
    circle = [-11, -15, 18]
    for i in range(3):
        circle[i] = Decimal(str(circle[i]))
    n = 1
    coefs = [4, -4]
    for i in range(n + 1):
        coefs[i] = Decimal(str(coefs[i]))
    x = Decimal(str(-4))
    print(find_L_R(x, coefs, circle))
    print(find_root(coefs, circle, x))



if __name__ == '__main__':
    test()

























