
class Node:
    """
    Класс - вершина бинарного дерева.
    Атрибуты:
        - ключ
        - ссылка на левого сына
        - ссылка на правого сына
        - ссылка на родителя
    """
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def clear_node(self):
        """Remove all references."""
        self.left = None
        self.right = None
        self.parent = None
        self.key = None

    def __str__(self):
        key = 'key = ' + str(self.key)
        if self.left is not None:
            left = 'left = ' + str(self.left.key)
        else:
            left = 'left = ' + 'None'
        if self.right is not None:
            right = 'right = ' + str(self.right.key)
        else:
            right = 'right = ' + 'None'
        if self.parent is not None:
            parent = 'parent = ' + str(self.parent.key)
        else:
            parent = 'parent = ' + 'None'
        return '(' + key + ', ' + left + ', ' + right + ', ' + parent + ')'


class SearchTree:
    """
    Класс - бинарное дерево поиска.
    Атрибуты:
        - множество всех вершин дерева
        - корень дерева
    """

    def __init__(self, tree=set()):
        self.tree = tree  # будет хранить множество всех вершин(просто для наглядности)
        self.root = None

    def print_tree(self):
        print('Tree:')
        for elem in self.tree:
            print(elem)

    def inorder(self, v: Node):
        if v is not None:
            SearchTree.inorder(self, v.left)
            print(v.key, end=' ')
            SearchTree.inorder(self, v.right)

    def search(self, r: Node, k):
        """
        Поиск ключа в дереве.
        :param r: корень дерева/поддерева, в котором будем искать
        :param k: ключ, который мы ищем
        :return: вершина(type=Node) c ключом k или,
                 если такого ключа нет, последняя вершина
                 при его поиске.
        """
        if k == r.key or r is None:
            return r
        while k != r.key:
            if k > r.key:
                if r.right is None:
                    return r
                r = r.right
            elif k < r.key:
                if r.left is None:
                    return r
                r = r.left
        return r

    def minimum(self, v: Node):
        """
        Поиск минимального ключа.
        :param v: корень дерева/поддерева, в котором будем искать
        :return: вершина(type=Node) с min значением ключа
        """
        if v.left is None:
            return v
        return SearchTree.minimum(self, v.left)

    def maximum(self, v: Node):
        """
        Поиск максимального ключа.
        :param v: корень дерева/поддерева, в котором будем искать
        :return: вершина(type=Node) с max значением ключа
        """
        if v.right is None:
            return v
        return SearchTree.maximum(self, v.right)

    def next(self, k):
        """
        Поиск следующего элемента.
        :param k: ключ
        :return: вершина(type=Node) со следующим по
                 возрастанию после k ключом.
        """
        root = self.root
        vertex = SearchTree.search(self, root, k)
        if vertex.right is not None:
            return SearchTree.minimum(self, vertex.right)
        father = vertex.parent
        while father is not None and vertex == father.right:
            vertex = father
            father = father.parent
        return father

    def prev(self, k):
        """
        Поиск предыдущего элемента.
        :param k: ключ
        :return: вершина(type=Node) с предшествующим
                 по возрастанию после k ключом.
        """
        root = self.root
        vertex = SearchTree.search(self, root, k)
        if vertex.left is not None:
            return SearchTree.maximum(self, vertex.left)
        father = vertex.parent
        while father is not None and vertex == father.left:
            vertex = father
            father = father.parent
        return father

    def insert(self, v: Node, k):
        """
        Вставка ключа в дерево.
        :param v: корень дерева, в которое нужно вставить ключ k
        :param k: новый ключ
        :return: не возвращает ничего, если вставка произошла успешно,
                 при попытке вставить существующий ключ, бросает исключение
        """
        if v is None:
            new = Node(k)
            self.root = new
            self.tree.add(new)
            return
        find_k = SearchTree.search(self, v, k)
        if find_k.key == k:
            raise KeyError('The element with key = ' + str(k) + ' already in tree')
        new = Node(k, left=None, right=None, parent=find_k)
        if k < find_k.key:
            assert find_k.left is None
            find_k.left = new
        elif k > find_k.key:
            assert find_k.right is None
            find_k.right = new
        self.tree.add(new)

    def delete(self, k):
        """
        Удаление ключа из дерева.
        :param k: ключ, который нужно удалить
        :return: не возвращает ничего, если удаление произошло успешно,
                 при попытке удалить несуществующий ключ, бросает исключение
        Разветвляется на 3 функции:
            1) удаляемая вершина это лист(не имеет детей)
            2) удаляемая вершина имеет только одного ребенка
            3) удаляемая вершина имеет двух детей
        """
        vertex = SearchTree.search(self, self.root, k)
        if vertex.key != k:
            raise KeyError('The key, you want to delete does not exist')

        # vertex это лист(нет детей):
        if (vertex.left is None) and (vertex.right is None):
            print('del vertex with no children')
            SearchTree.del_with_no_children(self, k, vertex)
        # у vertex есть только один ребенок:
        elif ((vertex.left is not None) and (vertex.right is None)) or \
                ((vertex.left is None) and (vertex.right is not None)):
            print('del vertex with only one child')
            SearchTree.del_with_only_one_child(self, k, vertex)
        # у vertex два ребенка:
        else:
            print('del vertex with two children')
            SearchTree.del_with_two_children(self, k, vertex)

    def del_with_no_children(self, k, vertex: Node):
        if vertex == self.root:  # если удаляемая вершина это корень
            self.root = None
            vertex.clear_node()
            self.tree.remove(vertex)
            return
        father = vertex.parent
        if father.left == vertex:
            father.left = None
        elif father.right == vertex:
            father.right = None

        vertex.clear_node()
        self.tree.remove(vertex)

    def del_with_only_one_child(self, k, vertex: Node):
        # определяю этого ребенка:
        if vertex.left is not None:
            child = vertex.left
        elif vertex.right is not None:
            child = vertex.right

        if vertex == self.root:  # если удаляемая вершина это корень
            child.parent = None
            self.root = child
            vertex.clear_node()
            self.tree.remove(vertex)
            return
        # меняю ссылки:
        father = vertex.parent
        if father.left == vertex:
            father.left = child
        elif father.right == vertex:
            father.right = child
        child.parent = father
        # удаляю vertex:
        vertex.clear_node()  # <=> vertex.left = None + vertex.right = None + vertex.parent = None
        self.tree.remove(vertex)

    def del_with_two_children(self, k, vertex: Node):
        # v_1 - самая правая вершина в левом поддереве вершины vertex
        delta = 0.0000000000001  # оочень маленькая
        v_1 = SearchTree.search(self, self.root, vertex.key - delta)
        # меняю их ключи(так проще)
        vertex.key = v_1.key
        if v_1.parent.left == v_1:
            v_1.parent.left = None
        elif v_1.parent.right == v_1:
            v_1.parent.right = None
        v_1.clear_node()
        self.tree.remove(v_1)












def draw_tree(v: Node):
    """
    Визуализация
    Работает с библиотекой binarytree.
    Принимает на вход корень дерева, которое нужно нарисовать
    """
    import binarytree
    def func(v: Node):
        if v is None:
            return None
        a = binarytree.Node(v.key, func(v.left), func(v.right))
        return a
    tree = func(v)
    print(tree)






def test1():
    a = Node(4)
    b = Node(2)
    c = Node(5)
    d = Node(1)
    e = Node(3)

    e.parent = b
    d.parent = b
    b.left = d
    b.right = e
    b.parent = a
    a.left = b
    c.parent = a
    a.right = c

    T = SearchTree({a, b, c, d, e})
    T.root = a
    r = T.root
    # T.print_tree()
    draw_tree(T.root)
    T.inorder(r)
    print()
    print(T.search(r, 6))
    print()
    print(T.next(3))
    print(T.prev(3))
    # T.print_tree()
    draw_tree(T.root)
    print()






def test2():
    t = SearchTree()
    t.insert(t.root, 12)
    print('root: ', t.root)
    # t.print_tree()
    draw_tree(t.root)
    t.insert(t.root, 4)
    print('root: ', t.root)
    t.insert(t.root, 20)
    t.insert(t.root, 2)
    t.insert(t.root, 8)
    t.insert(t.root, 7)
    t.insert(t.root, 10)
    t.insert(t.root, 61)
    t.insert(t.root, 40)
    t.insert(t.root, 53)
    t.insert(t.root, 14)
    print()
    # t.print_tree()
    draw_tree(t.root)
    t.inorder(t.root)
    



if __name__ == '__main__':
    test2()


















































