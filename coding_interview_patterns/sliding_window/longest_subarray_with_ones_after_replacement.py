class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        counter = {}
        counter[0] = 0
        counter[1] = 0
        max_len_sub = 0
        longest_sub = 0
        start = 0

        for end in range(len(arr)):
            current = arr[end]
            if current == 1:
                counter[current] += 1
            longest_sub = longest_sub if longest_sub > counter[current] else counter[current]

            if (end + 1 - start - longest_sub) > k:
                left_most = arr[start]
                counter[left_most] -= 1
                start += 1
            max_len_sub = max_len_sub if max_len_sub > end + 1 - start else end + 1 - start
        return max_len_sub
