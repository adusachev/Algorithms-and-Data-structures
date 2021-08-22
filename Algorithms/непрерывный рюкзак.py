# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:33:05 2020

@author: User
"""

"""
Первая строка содержит количество предметов n и вместимость рюкзака W
Каждая из следующих n строк задаёт стоимость c_i и объём w_i предмета
Выведите максимальную стоимость частей предметов 
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
"""

def main():
        n, W = map(int, input().split())
        price_mass = []
        while n != 0:
                ci, wi = map(int, input().split())
                price_mass.append((ci, wi))
                n -= 1


def bag(W: int, price_mass: list):
        """
        Выведите максимальную стоимость частей предметов 
        (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
        помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
        """
        price_mass.sort(key=lambda x: x[0]/x[1], reverse=True)
        ans = []
        steal_money = 0
        for i in range(len(price_mass)):
                ci = price_mass[i][0]
                wi = price_mass[i][1]
                if wi <= W:
                        ans.append((ci, wi))    # ans будет хранить все наши решения по отдельности
                        steal_money += ci
                        W -= wi       # оставшееся место в рюкзаке уменьшается
                elif W != 0:
                        wi_new = W
                        ci_new = W * (ci/wi)
                        ans.append((ci_new, wi_new))
                        steal_money += ci_new
                        W = 0       # обнуляю доступный вес в рюкзаке
        return steal_money




def test(bag):
        assert bag(0, [(60, 20)]) == 0
        assert bag(25, [(60, 20)]) == 60
        assert bag(25, [(60, 20), (0, 100)]) == 60
        assert bag(25, [(60, 20), (50, 50)]) == 60 + 5
        
        assert bag(50, [(60, 20), (100, 50), (120, 30)]) == 180
        
        from random import randint
        from timing import timed
        for attempt in range(100):
                n = randint(1, 1000)
                W = randint(0, 2*(10**6))
                price_mass = []
                for i in range(n):
                        price_mass.append(
                                (randint(0, 2*(10**6)), randint(1, 2*(10**6)))
                                )
                
                t = timed(bag, W, price_mass)
                assert t < 5

if __name__ == '__main__':
        main()
        test(bag)
        print(bag(W, price_mass))


















