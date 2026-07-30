class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = stone_sum // 2

        dp = {}

        def dfs(i, cur_sum):
            if i >= len(stones) or cur_sum >= target:
                return abs(cur_sum - (stone_sum - cur_sum))
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

            res = min(dfs(i + 1, cur_sum + stones[i]), dfs(i + 1, cur_sum))
            dp[(i, cur_sum)] = res

            return res

        return dfs(0, 0)

            

        
