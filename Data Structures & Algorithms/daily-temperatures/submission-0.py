class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            cur = temperatures[i]
            days = 0
            for j in range(i, len(temperatures)):
                if temperatures[j] > cur:
                    res.append(days)
                    break
                if i + days == len(temperatures) - 1:
                    res.append(0)
                    break
                days += 1
        return res