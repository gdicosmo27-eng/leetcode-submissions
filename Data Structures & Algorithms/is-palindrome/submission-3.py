class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        s = s.lower()

        while L <= R:
            while not s[L].isalnum() and L < R:
                L += 1
            while not s[R].isalnum() and R > L:
                R -= 1
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True
        