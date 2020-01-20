def count_on_bits(number):
    one_count = 0
    while number > 0:
        if (number & 1) > 0:
            one_count+=1
        number = number >> 1
    return one_count


