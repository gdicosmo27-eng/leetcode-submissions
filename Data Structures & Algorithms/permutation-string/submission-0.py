class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        cache1 = defaultdict(int)
        for char in s1:
            cache1[char] += 1
        
        for r in range(len(s1) - 1, len(s2)):
            cache2 = defaultdict(int)
            for char in s2[l:r + 1]:
                cache2[char] += 1
            if cache1 == cache2:
                return True
            l += 1
        
        return False
