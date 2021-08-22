


def merge(a: list, b: list):
    """
    Работает за O(len(a)+len(b))
    Сливает два отсортированных(!) массива в один
    Первым эл-том результирующего массива будет меньший из первых
    эл-тов данных массивов, оставшаяся часть мб заполнена рекурскивно
    """
    n1 = len(a)
    n2 = len(b)
    c = []
    i = 0
    j = n1   # конец массива а
    for t in range(n1 + n2):
        if i == n1:
            c.append(b[j - n1])
            j += 1
        elif j == n1 + n2:
            c.append(a[i])
            i += 1
        elif a[i] <= b[j - n1]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j - n1])
            j += 1
    return c



def merge_sort(a: list):
    """
    Сортировка слиянием
    (сортирует данный массив, а не возвращает отсортированный)
    """
    if len(a) <= 1:
        return [a[0]]
    middle = len(a) // 2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort(left)        # сортируем левые и правые части рекурсивно
    merge_sort(right)
    d = merge(left, right)
    for i in range(len(a)):
        a[i] = d[i]
    return d




def test():
    print(merge([7, 13], [1, 6]))
    print(merge_sort([7, 2, 5, 3, 7, 13, 1, 6, 0]))



if __name__ == '__main__':
    test()


    














































