# Write a function which takes two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. The characters in the first should appear without their order changing in the second string.


def forms_subsequence(str1, str2):
    result = ""
    str1_obj = {}
    for i, e in enumerate(str1):
        str1_obj[e] = e

    for i in str2:
        if str1_obj.get(i, None):
            result += i
            del str1_obj[i]

    if str1 in result:
        return True
    return False


print(forms_subsequence('abc', 'abracadabra'))
print(forms_subsequence('abc', 'acb'))