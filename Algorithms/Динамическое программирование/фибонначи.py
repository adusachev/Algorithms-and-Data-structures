

# сверху вниз
def fib_top_down(n: int):
    F = [-1] * (n + 1)
    if F[n-1] == -1:
        if n <= 1:
            F[n-1] = n
        else:
            F[n-1] = fib_top_down(n-1) + fib_top_down(n-2)
    return F[n-1]

print(fib_top_down(7))























