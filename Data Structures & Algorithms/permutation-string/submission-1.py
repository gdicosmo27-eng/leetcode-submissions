class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = defaultdict(int)
        for char in s1:
            need[char] += 1
        
        window = defaultdict(int)
        for i in range(len(s2)):
            window[s2[i]] += 1

            if i >= len(s1):
                left = s2[i - len(s1)]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
            
            if window == need:
                return True
        
        return False
            
