
# Ascending binary sorting.
# Consider an array of decimal int. Sort the int in asc order by the number of 1s in their binary representation.
# Elements having the same number of 1s in their binary rep are ordered by increasing decimal value

def count_on_bits(number):
    one_count = 0
    while number > 0:
        if (number & 1) > 0:
            one_count+=1
        number = number >> 1
    return one_count


def sortBySetBitCount(arr):
    bits_obj = {}
    for num in arr:
        val = count_on_bits(num)
        bits_obj[(val, num)] = num
    answer_arr = sorted(bits_obj.keys(), key=lambda a: (a[0], a[1]))
    return [item[1] for item in answer_arr]


print("** Ascending Binary Order: ")
print(sortBySetBitCount([4,5,9,7,6,1,2,3, 11,12, 13,14,15,16,17,18,19,20]))

