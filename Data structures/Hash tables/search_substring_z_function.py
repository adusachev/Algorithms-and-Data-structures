



def z_func_fast(s: str):
    """Эффективный алгоритм вычисления Z-функции. Сложность O(n)"""
    n = len(s)
    z = [0] * n
    L = 0
    R = 0
    for i in range(1, n):
        if i > R:
            while i+z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        elif i <= R:
            z[i] = min(R-i+1, z[i-L])
            while i+z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        L = i
        R = i + z[i] - 1
    return z






def search_substring_z(a: str, b: str):
    """
    Ищет все(!) индексы вхождения строки b в строку a
    Возвращает список индексов строки а, в которых начинается подстрока b
    """
    c = b + '#' + a  # добавляем невозможный символ разделитель
    z_function = z_func_fast(c)
    spisok = z_function[len(b)+1:]  # обрезаем результат z функции до длины строки a
    substring_length = max(spisok)
    if substring_length != len(b):
        return -1
    indexes = []
    for i in range(len(spisok)):
        if spisok[i] == substring_length:
            indexes.append(i)
    print(*indexes)



def test():
    pattern = 'aba'
    text = 'abacaba'
    search_substring_z(text, pattern)

def test2():
    pattern = 'Test'
    text = 'testTesttesT'
    search_substring_z(text, pattern)

def test3():
    pattern = 'aaaaa'
    text = 'baaaaaaa'
    search_substring_z(text, pattern)


def main():
    pattern = input()
    text = input()
    search_substring_z(text, pattern)

if __name__ == '__main__':
    test()

















