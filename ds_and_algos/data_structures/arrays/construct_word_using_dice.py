"""

Given a word of length n and n six-sided dice with a character in each side. Find out if this word can be constructed by the set of given dice.

Example 1:
Input:
word = "hello"
dice = [[a, l, c, d, e, f], [a, b, c, d, e, f], [a, b, c, h, e, f], [a, b, c, d, o, f], [a, b, c, l, e, f]]
Output: true
Explanation: dice[2][3] + dice[1][4] + dice[0][1] + dice[4][3] + dice[3][4]


Example 2:

Input:
word = "hello"
dice = [[a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f]]
Output: false

Example 3:

Input:
word = "aaaa"
dice = [[a, a, a, a, a, a], [b, b, b, b, b, b], [a, b, c, d, e, f], [a, b, c, d, e, f]]
Output: false

"""


from collections import Counter

def can_roll(word, dice):
    def helper(word, word_counter, dice, dice_i):
        if not word: return True

        for i, char in enumerate(word):
            if char in dice[dice_i]:
                word_counter[char] -= 1
                if word_counter[char] == 0: word_counter.pop(char)

                ans = helper(word[:i] + word[i + 1:], word_counter, dice, dice_i + 1)

                if ans: return True

                if char not in word_counter: word_counter[char] = 1
                else: word_counter[char] += 1

        return False

    return helper(word, Counter(word), dice, 0)


if __name__ == '__main__':
    word = 'hello'
    dice1 = [['a', 'l', 'c', 'd', 'e', 'f'],
             ['a', 'b', 'c', 'd', 'e', 'f'],
             ['a', 'b', 'c', 'h', 'e', 'f'],
             ['a', 'b', 'c', 'd', 'o', 'f'],
             ['a', 'b', 'c', 'l', 'e', 'f']]
    dice2 = [['a', 'b', 'c', 'd', 'e', 'f'],
             ['a', 'b', 'c', 'd', 'e', 'f'],
             ['a', 'b', 'c', 'd', 'e', 'f'],
             ['a', 'b', 'c', 'd', 'e', 'f'],
             ['a', 'b', 'c', 'd', 'e', 'f']]
    dice3 = [['a', 'a', 'a', 'a', 'a', 'a'],
             ['b', 'b', 'b', 'b', 'b', 'b'],
             ['a', 'b', 'c', 'd', 'e', 'f'],
             ['a', 'b', 'c', 'd', 'e', 'f']]
    print(can_roll('aaaa', dice3))