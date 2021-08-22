



def hoar_sort(a):
    """изменяет исходный список, а не возвращает отсортированный"""
    if len(a) <= 1:
        return
    barrier = a[0]    # нужно взять случайный барьерный элемент, мы возьмем первый
    L = []            # L = M = R = [] так писать нельзя
    M = []
    R = []
    for x in a:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        a[k] = x
        k += 1


def main():
    w = [4, 6, 7, 2, 4, 0, 9]
    hoar_sort(w)
    print(w)

if __name__ == '__main__':
    main()




















