class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open_count, close_count = 0, 0
        max_length = 0
        
        # 0 to n traversal
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                open_count += 1
            else:
                close_count += 1
                
            if open_count == close_count:
                length = open_count + close_count
                max_length = max(max_length, length)
            elif close_count > open_count:
                open_count = close_count = 0
        
        # n to 0 traversal
        open_count = close_count = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '(':
                open_count += 1
            else:
                close_count += 1
                
            if open_count == close_count:
                length = open_count + close_count
                max_length = max(max_length, length)
            elif open_count > close_count:
                open_count = close_count = 0
        
        return max_length
