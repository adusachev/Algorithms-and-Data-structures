
class Element:
    """
    Класс - элемент двусвязного списка.
    Каждый экземпляр класса хранит:
        - данные
        - ссылку на следующий эл-т
        - ссылку на предыдущий эл-т
    """

    def __init__(self, value=None, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev

    def __str__(self):
        value = str(self._value)
        if self._next is None:
            next = 'None'
        else:
            next = str(self._next._value)
        if self._prev is None:
            prev = 'None'
        else:
            prev = str(self._prev._value)
        ans = '(' + 'value = ' + value + ', ' \
                    + 'next = ' + next + ', '\
                    + 'prev = ' + prev + ')'
        return ans


class DoublyLinkedList:
    """
    Класс - двусвязный список.
    Определены операции:
        - добавление и удаление в любое место списка за О(1)
          (для середины есть нюансы)
        - получение эл-та списка по индексу за О(n)
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def push_front(self, x):
        """Добавление в начало списка"""
        self._length += 1
        if self._head is None:  # если список пуст
            # получаем список из одного эл-та:
            self._head = self._tail = Element(value=x, next=None, prev=None)
        else:
            new = Element(value=x, next=self._head, prev=None)
            prev_head = self._head
            prev_head._prev = new
            self._head = new

    def push_back(self, x):
        """Добавление в конец списка"""
        self._length += 1
        if self._head is None:
            # получаем список из одного эл-та:
            self._head = self._tail = Element(value=x, next=None, prev=None)
        else:
            new = Element(x, next=None, prev=self._tail)  # вставленный эл-т
            prev_tail = self._tail  # старый хвост
            # меняю ссылку старого хвоста с None на new:
            prev_tail._next = new
            self._tail = new  # обновляю значение хвоста

    def pop_front(self):
        """Удаляет эл-т из начала списка и возвращает его"""
        assert self._head is not None, "List is empty"
        self._length -= 1
        x = self._head._value
        # обновляю ссылки:
        self._head = self._head._next
        self._head._prev = None
        return x

    def print_elems(self):
        """Выводит все эл-ты списка по порядку"""
        elem = self._head
        while elem is not None:
            print(elem._value, end=' ')
            elem = elem._next
        print()




    def pop(self):
        """Удаляет эл-т из конца списка и возвращает его"""
        assert self._head is not None, "List is empty"
        self._length -= 1
        x = self._tail._value
        # обновляю ссылки:
        self._tail = self._tail._prev
        self._tail._next = None
        return x

    def insert_after(self, x, elem):
        """Вставка эл-та x в любое место после(!) заданного эл-та списка elem"""
        if elem == self._tail:
            print('Use push_back(x)')
            return
        self._length += 1
        elem2 = elem._next  # эл-т, следующий за elem
        new = Element(value=x, next=elem2, prev=elem)  # вставленный эл-т
        # обновляю ссылки:
        elem._next = new
        elem2._prev = new

    def insert_before(self, x, elem):
        """Вставка эл-та x в любое место перед(!) заданным эл-том списка elem"""
        if elem == self._head:
            print('Use push_front(x)')
            return
        self._length += 1
        elem2 = elem._prev
        new = Element(value=x, next=elem, prev=elem2)
        # обновляю ссылки:
        elem._prev = new
        elem2._next = new

    def delete_after(self, elem):
        """
        Удаляет эл-т, следующий за заданным эл-том списка elem.
        При попытке удалить последний эл-т просит использовать pop()
        """
        if elem == self._tail:
            print('There is no elements after elem, try again')
            return
        if elem._next == self._tail:
            print('Use pop()')
            return
        self._length -= 1
        deleted = elem._next
        new_next = deleted._next  # эл-т, следующий за удаленным
        elem._next = new_next
        new_next._prev = elem

    def delete_before(self, elem):
        """
        Удаляет эл-т, следующий перед заданным эл-том списка elem
        При попытке удалить первый эл-т просит использовать pop_front()
        """
        if elem == self._head:
            print('There is no elements before elem, try again')
            return
        if elem._prev == self._head:
            print('Use pop_front()')
            return
        self._length -= 1
        deleted = elem._prev
        new_prev = deleted._prev
        elem._prev = new_prev
        new_prev._next = elem

    def get_elem(self, index):
        """Выводит эл-т списка с индексом index. Время - О(n)."""
        assert 0 <= index < self._length, 'That index not exist'
        current = self._head
        for i in range(index):
            if current is None:
                return None
            current = current._next
        return current










def test():
    a = DoublyLinkedList()
    a.push_front(5)
    a.push_front(6)
    a.push_front(7)
    a.push_back(1)
    a.print_elems()
    print(a.pop_front())
    a.print_elems()
    print(a._length)
    print()


def test2():
    a = DoublyLinkedList()
    a.push_front(5)
    a.push_front(6)
    a.push_front(7)
    a.push_back(1)
    a.push_back(10)
    a.push_front(15)
    a.print_elems()
    print()

    print(a.pop_front())
    print(a.pop())
    a.print_elems()
    a.push_back(10)
    a.push_front(15)
    print()

    a.print_elems()




def test3():
    a = DoublyLinkedList()
    a.push_front(5)
    a.push_front(6)
    a.push_front(7)
    a.push_back(1)
    a.push_back(10)
    a.push_front(15)
    a.print_elems()

    y = a.get_elem(3)  # определение элемента - О(n)
    print(y)
    print()

    a.insert_after(10000, y)  # вставка после - О(1)
    a.print_elems()
    a.insert_before(100000, y)  # вставка до - О(1)
    a.print_elems()
    print(y)
    print()

    a.delete_after(y)
    a.print_elems()
    a.delete_before(y)
    a.print_elems()
    print(y)



def test4():
    a = DoublyLinkedList()
    a.push_front(5)
    a.push_front(6)
    a.push_front(7)
    a.push_back(1)
    a.push_back(10)
    a.push_front(15)
    a.print_elems()

    y = a.get_elem(2)
    print(y)
    a.delete_before(y)
    a.print_elems()




if __name__ == '__main__':
    test3()





































