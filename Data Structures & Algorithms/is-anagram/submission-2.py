class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_first = [0] * 26
        for c in s:
            count_first[ord(c) - ord('a')] += 1
        
        count_second = [0] * 26
        for c in t:
            count_second[ord(c) - ord('a')] += 1

        return count_first == count_second
