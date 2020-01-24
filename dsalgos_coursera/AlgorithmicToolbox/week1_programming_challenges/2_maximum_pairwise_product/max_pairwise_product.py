# python3

def max_pairwise_product(n, numbers):
    if n != len(numbers):
        return

    max_index = -1
    max_index2 = -1
    for i in range(n):
        if max_index == -1 or (numbers[i] > numbers[max_index]):
            max_index = i

    for j in range(n):
        if j != max_index and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j

    return numbers[max_index] * numbers[max_index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_n, input_numbers))
