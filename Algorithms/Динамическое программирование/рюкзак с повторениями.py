


def knapsack_with_reps(W: int, weights: list, costs: list):
    """
    :param W: вместимость рюкзака(целое)
    :param weights: веса предметов(целые)
    :param costs: стоимости предметов(целые)
    :return: max стоимость предметов суммарного веса не более W (с возможностью повторения предметов)
    """
    d = [0] * (W + 1)
    n = len(weights)
    for w in range(1, W + 1):
        for i in range(0, n):
            w_i = weights[i]
            c_i = costs[i]
            if w_i <= w:
                d[w] = max(d[w], d[w-w_i] + c_i)
    return d[-1]


def test():
    assert knapsack_with_reps(0, [2, 4, 6], [45, 23, 67]) == 0
    assert knapsack_with_reps(5, [5], [23]) == 23
    assert knapsack_with_reps(5, [10], [34]) == 0
    assert knapsack_with_reps(10, [6, 3, 4, 2], [30, 14, 16, 9]) == 48


if __name__ == '__main__':
    test()





































