class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxFreq = 0

        L = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxFreq = max(maxFreq, count[s[R]])
            if ((R - L) + 1) - maxFreq > k:
                count[s[L]] -= 1
                L += 1
        
        return (R - L) + 1


