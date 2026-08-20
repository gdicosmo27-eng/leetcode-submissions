class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        if digits == "":
            return []

        res = []

        def helper(cur_string, idx):
            if len(cur_string) == len(digits):
                res.append("".join(cur_string))
                return
            
            for c in digit_map[digits[idx]]:
                cur_string.append(c)
                helper(cur_string, idx + 1)
                cur_string.pop()

        helper([], 0)
        return res