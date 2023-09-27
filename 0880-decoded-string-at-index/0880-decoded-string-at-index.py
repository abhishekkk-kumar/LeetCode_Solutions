class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        word_length = 0
        for char in s:
            if char.isalpha():
                word_length += 1
            else:
                word_length *= int(char)
        
        for char in s[::-1]:
            k %= word_length
            if char.isalpha():
                if k == 0:
                    return char
                else:
                    word_length -= 1
            else:
                word_length //= int(char)
        