


def bin_sum(a: int, b: int):
    a = str(a)
    b = str(b)
    if len(a) > len(b):
        b += (len(a)-len(b)) * '0'
    else:
        a += (len(b) - len(a)) * '0'
    c = ''
    tmp = ''
    for i in range(len(a)-1, -1, -1):
        if a[i] == b[i] == '1' and len(tmp) == 0:
            c += '0'
            tmp += '1'
        elif len(tmp) == 0:
            c += str(max(int(a[i]), int(b[i])))
        else:
            if int(a[i]) + int(b[i]) == 1:
                c += '0'
            if a[i] == b[i] == '0':
                c += '1'
                tmp = ''
            elif a[i] == b[i] == '1':
                c += '1'
    c += tmp
    return c[::-1]

a = 110101
b = 100011
print(bin_sum(a, b))


def multiply(x: int, y: int):
    """умножение двух двоичных чисел"""
    if y == 0:
        return 0
    z = multiply(x, y//10)
    if y % 10 == 0:
        return z * 10
    else:
        return int(bin_sum(x, z*10))

x = 1101
y = 1011
print(multiply(x, y))


def Karatsuba(x: int, y: int):
    """алгоритм Карацубы (быстрое умножение чисел)"""
    n = max(len(str(x)), len(str(y)))
    if n == 1:
        return x*y
    left = n//2
    right = n//2
    x_L = x // 10**left
    x_R = x % 10**right
    y_L = y // 10**left
    y_R = y % 10**right
    p1 = Karatsuba(x_L, y_L)
    p2 = Karatsuba(x_R, y_R)
    p3 = Karatsuba(x_L + x_R, y_L + y_R)
    return p1 * 2**(2*n//2) + (p3 - p1 - p2) * 2**(n//2) + p2

print(Karatsuba(10111, 11001))










































