class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        L, maxLength = 0, 0

        for R in range(len(s)):
            if s[R] not in cache:
                cache[s[R]] = R
                if (R - L) + 1 > maxLength:
                    maxLength = (R - L) + 1
            else:
                if L > cache[s[R]]:
                    cache[s[R]] = R
                    if (R - L) + 1 > maxLength:
                        maxLength = (R - L) + 1
                else:
                    L = cache[s[R]] + 1
                    cache[s[R]] = R
        
        return maxLength
                
        