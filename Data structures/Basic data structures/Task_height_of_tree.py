

def leaves(parents: list):
    """
    :param parents: список родителей (где -1 указывает на корень)
    :return: список лисьтев данного дерева
    """
    parents_set = set(parents)
    parents_set.remove(-1)
    all_set = set(range(0, len(parents)))
    tree_leaves = all_set - parents_set
    return list(tree_leaves)

# сдал, работает
def height(parents: list, root: int):
    """
    Итеративный алгоритм (быстрый)
    :param parents: список родителей (где -1 указывает на корень)
    :param root: корень дерева, высоту которого нужно вычислить
    :return: высоту дерева до данного корня
    """
    # ans будет хранить значение высоты дерева до вершины r = i, где i - индексы в ans
    ans = [0] * len(parents)
    if len(ans) == 1:
        return 1
    for leaf in leaves(parents):
        ans[leaf] = 1
        roditel = parents[leaf]
        # отсекаем ненужные пробеги по дереву:
        if ans[roditel] < 2:  # заходим в случае когда высоту родителя листа стоит обновлять
            ans[roditel] = 2
            while roditel != root:  # "рекурсивно" идем вверх по дереву
                child = roditel
                roditel = parents[child]
                # отсекаем ненужные пробеги по дереву:
                if (ans[child] + 1) <= ans[roditel]:
                    # случай, когда не нужно обновлять значение высоты, выхожу из цикла:
                    roditel = root
                else:
                    ans[roditel] = ans[child] + 1
    # print(ans)
    return ans[root]




def test():
    parents = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
    # print(leaves(parents))
    print(height(parents, 9))

def test1():
    parents = [2, 2, 3, 5, 5, 7, 7, 9, 9, -1]
    # print(leaves(parents))
    print(height(parents, 9))

def test2():
    parents = [-1, 0, 4, 0, 3]
    # print(leaves(parents))
    print(height(parents, 0))


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    root = parents.index(-1)
    print(height(parents, root))

if __name__ == '__main__':
    test1()




















