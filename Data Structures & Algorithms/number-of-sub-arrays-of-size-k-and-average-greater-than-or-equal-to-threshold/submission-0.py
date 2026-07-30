import statistics
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        total = 1 if (window_sum / k) >= threshold else 0

        for R in range(k, len(arr)):
            window_sum += arr[R] - arr[R - k]
            if (window_sum / k) >= threshold:
                total += 1

        return total
            
