class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        L, maxLength = 0, 0

        for R in range(len(s)):
            if s[R] in cache and L <= cache[s[R]]:
                L = cache[s[R]] + 1
            cache[s[R]] = R
            maxLength = max(maxLength, (R - L) + 1)
        
        return maxLength
                
        