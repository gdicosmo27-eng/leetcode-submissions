class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = []
        if digits == "":
            return []

        lettermap = {}
        lettermap["2"] = "abc"
        lettermap["3"] = "def"
        lettermap["4"] = "ghi"
        lettermap["5"] = "jkl"
        lettermap["6"] = "mno"
        lettermap["7"] = "pqrs"
        lettermap["8"] = "tuv"
        lettermap["9"] = "wxyz"

        def helper(i, digits, currComb, combs):
            if len(currComb) == len(digits):
                combs.append(currComb)
                return
            if i >= len(digits):
                return
            
            for j in range(len(lettermap[digits[i]])):
                currComb += lettermap[digits[i]][j]
                helper(i + 1, digits, currComb, combs)
                currComb = currComb[:-1]
        
        helper(0, digits, "", combs)
        return combs