n = int(input())
a = list(map(int, input().split()))

def npp(a: list):
    """
    :param a: исходная последовательность
    :return: ans - длина НВП, elements - сама НВП(восстановление без prev)
    """
    n = len(a)
    d = [-1] * n
    for i in range(0, n):
        d[i] = 1
        for j in range(0, i):
            if a[i] % a[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    ans = max(d)
    # print(d)
    return ans

# a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
# print(a)
print(npp(a))

































































