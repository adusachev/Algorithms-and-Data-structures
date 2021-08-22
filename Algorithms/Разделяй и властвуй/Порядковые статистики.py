
import random

def random_select(a: list, k: int):
    """
    :return: k-й эл-т упорядоченного по неубыванию массива(т. е. b[k], где b = sorted(a))
    """
    if len(a) == 1:
        return a[0]
    t = random.randint(0, len(a) - 1)
    x = a[t]
    left = []
    middle = []
    right = []
    for elem in a:
        if elem < x:
            left.append(elem)
        elif elem == x:
            middle.append(elem)
        else:
            right.append(elem)
    m1 = len(left)     # длина левой части
    m2 = m1 + len(middle)  # длина левой части + серединки
    if 0 <= k <= m1 - 1:
        return random_select(left, k)
    elif m1 <= k <= m2 - 1:
        return x
    else:
        return random_select(right, k - m2)   # важно в рекурсивном вызове сделать сдвиг на длину части которая уже не пригодится(левая+серединка)

a = [999, 44, 123]
k = 1
ans = random_select(a, k)
print(ans)

# проверка
b = sorted(a)
print(ans == b[k])
























































