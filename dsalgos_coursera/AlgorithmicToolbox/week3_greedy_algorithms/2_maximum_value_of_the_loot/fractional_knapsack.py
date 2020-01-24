# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    arr = [(v, w) for v, w in zip(values, weights)]

    w_v = sorted(arr, key=lambda item: (item[0] / item[1]), reverse=True)
    max_capacity = int(capacity)


    for item in w_v:
        val = item[0]
        weight = item[1]
        if (max_capacity - weight) < 0:
            value += (val / weight) * max_capacity
            max_capacity = 0
        else:
            max_capacity -= weight
            value += val

        if not max_capacity:
            return value

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
