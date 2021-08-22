# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:37:56 2020

@author: User
"""




def BinarySearch(a: list, k):
        """
        Parameters
        ----------
        a : list
                упорядоченный по неубыванию массив.
        k : int
                число, индекс которого мы ищем.
        Returns:
                индекс i, такой что a[i] = k, или -1, если такого i нет.
        """
        # Invariant: L <= m <= R
        L = 0
        R = len(a) - 1
        while R - L >= 0:
                m = (R + L) // 2    # центр отрезка (L, R)
                if k > a[m]:
                        L = m + 1
                elif k < a[m]:
                        R = m - 1     # аналогично L = m + 1
                else:
                        return m
        return -1


def main():
        a = [1, 2, 3, 4, 5, 6]
        k = 6
        print(BinarySearch(a, k))


# тест на краевые случаи
def test():
        assert BinarySearch([], 42) == -1
        assert BinarySearch([42], 42) == 0
        assert BinarySearch([42], 24) == -1
        

if __name__ == '__main__':
        test()
        main()

























