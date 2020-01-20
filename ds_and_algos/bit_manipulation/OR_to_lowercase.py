class Solution:
    def toLowerCase(self, str: str) -> str:
        answer = ""
        for letter in str:
            answer += chr(ord(letter) | ord(" "))

        return answer