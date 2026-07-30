class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        if digits == "":
            return []

        lettermap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz", 
        }

        def helper(i, currComb):
            if len(currComb) == len(digits):
                combs.append(currComb)
                return
            if i >= len(digits):
                return
            
            for c in lettermap[digits[i]]:
                helper(i + 1, currComb + c)
        
        helper(0, "")
        return combs