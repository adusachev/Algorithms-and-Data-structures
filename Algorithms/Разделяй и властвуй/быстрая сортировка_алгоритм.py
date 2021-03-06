
def quick_sort(a: list, L: int, R: int):
    """
    не возвращает ничего, изменяет данный массив а (сортирует)
    """
    if L >= R:
        return
    m = partition(a, L, R)
    quick_sort(a, L, m)
    quick_sort(a, m + 1, R)


def partition(a: list, L: int, R: int):
    """
    :param a: список
    :param L: левая граница списка
    :param R: правая граница списка
    :return: возвращает индекс j, изменяет массив а так что опорный эл-т становится на позицию j
             и a[j] = b[j] (если бы b = sorted(a))
    """
    x = a[L]
    j = L
    for i in range(L + 1, R):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]   # если текущий эл-т меньше опорного, кидаю его в зону меньших эл-тов(надо смотреть картинку в тетради а то какая то непонтная хуйня здесь происходит)
    a[L], a[j] = a[j], a[L]    # меняю опорный эл-т с последним эл-том который меньше его(см тетрадь)
    # print(j)
    return j

a = [3, 1, 4, 5, 2, 2, 2, 8]


quick_sort(a, 0, len(a))
print(a)






















































