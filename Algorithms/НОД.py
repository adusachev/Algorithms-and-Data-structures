# -*- coding: utf-8 -*-

a, b = map(int, input().split())

def gcd_primitive(a, b):
        assert a >= 0 and b >= 0
        for d in reversed(range(max(a, b)+1)):
                if d == 0 or a % d == b % d == 0:
                        return d
                
def gcd_optimal(a, b):
        """Алгоритм Евклида"""
        if a == 0:
                return b
        elif b == 0:
                return a
        if a >= b:
                return gcd_optimal(a % b, b)
        if b >= a:
                return gcd_optimal(a, b % a)
        
print(gcd_optimal(a, b), gcd_primitive(a, b))

import random

def test(gcd, n_iter=100):
        for i in range(n_iter):
                c = random.randint(0, 1024)
                a = c * random.randint(0, 128)
                b = c * random.randint(0, 128)
                assert gcd(a, a) == gcd(a, 0) == a
                assert gcd(b, b) == gcd(b, 0) == b
                assert gcd(a, 1) == gcd(b, 1) == 1
                d = gcd(a, b)
                assert a % d == b % d == 0

test(gcd_optimal)
test(gcd_primitive)


from timing import timed
print(timed(gcd_optimal, a, b))
print(timed(gcd_primitive, a, b))


































