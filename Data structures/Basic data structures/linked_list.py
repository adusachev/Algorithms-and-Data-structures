
class Element:
    """
    Класс - элемент односвязного списка.
    Каждый экземпляр класса хранит:
        - данные
        - ссылку на следующий эл-т
    """

    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next




class LinkedList:
    """
    Класс - односвязный список.
    Определены операции:
        - добавление в начало списка за О(1)
        - добавление в конец списка за О(1)
        - удаление из начала списка за О(1)
    Все остальные операции будут стоить O(n).
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def push_front(self, x):
        """Добавление в начало списка"""
        self._length += 1
        self._head = Element(x, self._head)
        if self._tail is None:  # если список пуст, обновляем его конец
            # получаем список из одного эл-та:
            self._tail = self._head

    def push_back(self, x):
        """Добавление в конец списка"""
        self._length += 1
        if self._head is None:
            # получаем список из одного эл-та:
            self._head = self._tail = Element(x, None)
        else:
            new = Element(x, None)  # вставленный эл-т
            prev_tail = self._tail  # старый хвост
            # меняю ссылку старого хвоста с None на new:
            prev_tail._next = new
            self._tail = new  # обновляю значение хвоста

    def pop_front(self):
        """Удаляет эл-т из начала списка и возвращает его"""
        assert self._head is not None, "List is empty"
        x = self._head._value
        self._head = self._head._next
        self._length -= 1
        return x

    def print_elems(self):
        """Выводит все эл-ты списка по порядку"""
        elem = self._head
        while elem is not None:
            print(elem._value, end=' ')
            elem = elem._next
        print()

    def list_length(self):
        return self._length




def test():
    a = LinkedList()
    a.push_front(5)
    a.push_front(6)
    a.push_front(7)
    a.push_back(1)
    a.print_elems()
    print(a.pop_front())
    a.print_elems()
    print(a.list_length())


if __name__ == '__main__':
    test()






































