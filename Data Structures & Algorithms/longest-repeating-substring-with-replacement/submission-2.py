class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxfreq = 0, 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            maxfreq = max(maxfreq, count[s[r]])
            if ((r - l) + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
        
        return (r - l + 1)