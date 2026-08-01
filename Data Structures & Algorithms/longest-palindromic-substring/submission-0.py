class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = [0, (0, 0)]

        for i in range(len(s)):
            # Odd
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if longest[0] < (R - L + 1):
                    longest = [R - L + 1, (L, R)]
                L -= 1
                R += 1

            # Even
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if longest[0] < (R - L + 1):
                    longest = [R - L + 1, (L, R)]
                L -= 1
                R += 1
        
        L, R = longest[1]
        return s[L:R + 1]
