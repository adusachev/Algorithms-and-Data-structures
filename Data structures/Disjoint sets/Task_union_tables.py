
class TablesSet:
    """
    По сути, не отличается от DisjointSet.
    Нужно убрать объединение по рангам, иначе ничего не получится.
    Здесь в parent необходимо хранить доп информацию, поэтому создаем словарь,
    и делаем все нужные обращения по ключу father.
    Добавил два вспомогательных метода для вычисления ответа.
    """

    def __init__(self):
        self.parent = []  # i-й эл-т будет хранить индекс своего корня и размер i-ой таблицы
        self.max = []  # будет хранить в себе финальный ответ - значения максимумов


    def make_set(self, elem):
        i = elem['father']
        while len(self.parent) - 1 < i:
            self.parent.append(float('inf'))
        self.parent[i] = elem


    def find(self, i):
        if i != self.parent[i]['father']:
            self.parent[i]['father'] = TablesSet.find(self, self.parent[i]['father'])
        return self.parent[i]['father']

    # вершина j подвешивается к вершине i (!)
    def union(self, i, j):
        i_id = TablesSet.find(self, i)
        j_id = TablesSet.find(self, j)
        if i_id == j_id:
            TablesSet.update_max(self, i_id)
            return
        self.parent[j_id]['father'] = i_id

        self.parent[i_id]['size'] += self.parent[j_id]['size']
        self.parent[j_id]['size'] = 0

        TablesSet.update_max(self, i_id)

    # При необходимости обновляет макс значение и добавлет его в массив с ответами
    # (используется только в union)
    def update_max(self, i_id):
        if self.parent[i_id]['size'] > self.max[-1]:
            self.max.append(self.parent[i_id]['size'])
        else:
            self.max.append(self.max[-1])

    # Определяет макс размер среди всех таблиц (запускается один раз в начале и все)
    def determine_max(self):
        ans = 0
        for i in range(1, len(self.parent)):
            if self.parent[i]['size'] > ans:
                ans = self.parent[i]['size']
        self.max.append(ans)










def func(n: int, m: int, r: list, requests: list):

    tables = TablesSet()
    for i in range(1, n+1):
        # i-й эл-т будет хранить индекс своего корня("отца") и размер i-ой таблицы
        tables.make_set({'father': i, 'size': r[i]})

    tables.determine_max()

    for i in range(1, m + 1):
        who_to_hang = requests[i][1]
        where_to_hang = requests[i][0]
        tables.union(where_to_hang, who_to_hang)

    # финальный ответ к задаче:
    for i in range(1, len(tables.max)):
        print(tables.max[i])




def main():
    # Везде делаю нулевой эл-т None чтобы было удобней ориентироваться по индексам
    # Это немного усложняет основную функцию, тк везде обязательно надо итерироваться с единицы
    n, m = map(int, input().split())
    r = [None]
    r.extend(list(map(int, input().split())))
    requests = [None]
    m1 = m
    while m1 != 0:
        destination, source = map(int, input().split())
        requests.append((destination, source))
        m1 -= 1

    func(n, m, r, requests)


def test():
    n = 5
    m = 5
    r = [None, 1, 1, 1, 1, 1]
    requests = [None,
                (3, 5),
                (2, 4),
                (1, 4),
                (5, 4),
                (5, 3)]
    func(n, m, r, requests)


def test2():
    n = 6
    m = 4
    r = [None, 10, 0, 5, 0, 3, 3]
    requests = [None,
                (6, 6),
                (6, 5),
                (5, 4),
                (4, 3)]
    func(n, m, r, requests)



if __name__ == '__main__':
    test()

































































