



def calc(n: int):
    d = [0] * (n+1)
    operations = [0, 1]

    for i in range(2, n+1):
        add_1 = d[i-1] + 1
        mult_2 = float('inf')
        mult_3 = float('inf')
        if i % 2 == 0:
            mult_2 = d[i//2] + 1
        if i % 3 == 0:
            mult_3 = d[i//3] + 1
        d[i] = min(add_1, mult_2, mult_3)
        # дальше восст ответа
        if d[i] == add_1:
            operations.append('add_1')
        elif d[i] == mult_2:
            operations.append('mult_2')
        elif d[i] == mult_3:
            operations.append('mult_3')

    def get_answer(operations: list, ans: int):
        if ans == 0:
            return
        step = operations[ans]
        if step == 'add_1':
            get_answer(operations, ans-1)
        if step == 'mult_2':
            get_answer(operations, ans//2)
        if step == 'mult_3':
            get_answer(operations, ans//3)
        print(ans, end=' ')

    print(d[-1])
    get_answer(operations, n)
    return

def test():
    calc(5)

def test2():
    calc(96234)

def main():
    n = int(input())
    calc(n)

test2()











































