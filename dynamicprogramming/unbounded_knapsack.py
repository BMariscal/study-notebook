
def unbounded_knapsack(values, weights, max_capacity):
    value = 0
    arr = [(v, w) for v, w in zip(values, weights)]

    w_v = sorted(arr, key=lambda item: item[0] // item[1], reverse=True)

    for item in w_v:
        val = item[0]
        weight = item[1]
        if (max_capacity - weight) < 0:
            value += (val // weight) * max_capacity
            max_capacity = 0
        else:
            max_capacity = max_capacity - weight
            value += val

        if not max_capacity:
            return value
    return value



a = unbounded_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8)
print(a == 140)

b = unbounded_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6)
print(b == 106)

c = unbounded_knapsack([60, 40, 100, 120], [10, 40, 20, 30], 50)
print(c == 240)

d = unbounded_knapsack([60, 100, 120], [10, 20, 30], 50)
print(d == 240)