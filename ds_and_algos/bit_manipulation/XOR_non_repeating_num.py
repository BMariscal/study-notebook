class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """

        Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        If we take XOR of zero and some bit, it will return that bit
        If we take XOR of two same bits, it will return 0

        """
        a = 0
        for i in nums:
            a ^= i
        return a


"""
Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
"""