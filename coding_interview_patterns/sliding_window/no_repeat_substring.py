class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        longest_substring = 0
        letter_counter = {}

        for window_end in range(len(s)):
            if s[window_end] in letter_counter:
                window_start = max(window_start, letter_counter[s[window_end]]+1)

            letter_counter[s[window_end]] = window_end
            longest_substring = max(longest_substring, window_end - window_start+1)
        return longest_substring
