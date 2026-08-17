class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combos, cur_combo = [], []

        def backtrack(i, total):
            if total == target:
                combos.append(cur_combo.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            cur_combo.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            cur_combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return combos