class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        l, maxlength = 0, 0

        for r in range(len(s)):
            if s[r] in cache and l <= cache[s[r]]:
                l = cache[s[r]] + 1
            cache[s[r]] = r
            maxlength = max(maxlength, (r - l + 1))

        return maxlength

        

        
            