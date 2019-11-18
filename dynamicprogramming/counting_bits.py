def countBits(num):
    result = [0]
    for i in range(1, num + 1):
        if i % 2 == 0:
            result.extend([result[i >> 1]])
        else:
            result.extend([result[i - 1] + 1])
    return result