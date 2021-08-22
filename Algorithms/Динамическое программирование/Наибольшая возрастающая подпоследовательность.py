

def LIS_bottom_up(a: list):
    """
    :param a: исходная последовательность
    :return: ans - длина НВП, elements - сама НВП(восстановление без prev)
    """
    n = len(a)
    d = [-1] * n
    for i in range(0, n):
        d[i] = 1
        for j in range(0, i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = max(d)

    # восстановление ответа:
    k = 0
    for i in range(1, n):
        if d[i] > d[k]:
            k = i      # ищем индекс места где d имеет максимум
    max_len = d[k]  # длина подпосл-ти, кончающейся в эл-те и индексом k

    elements = [a[k]]
    while max_len > 0:
        max_len -= 1
        for i in range(k-1, -1, -1):
            if d[i] == max_len and a[i] < a[k]:
                k = i
                elements.append(a[k])

    print(d)
    elements.reverse()
    print(elements)
    return ans

a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
# a = [1, 2, 3, 4, 5, 2, 3, 77, 1, 2, 4, 5, 9, 10, 4]
print(a)

print(LIS_bottom_up(a))






























































