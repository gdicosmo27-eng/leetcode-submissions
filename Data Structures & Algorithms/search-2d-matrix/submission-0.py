class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one = []
        for mat in matrix:
            one += mat

        left, right = 0, len(one) - 1

        while left <= right:
            mid = (right + left) // 2

            if one[mid] > target:
                right = mid - 1
            elif one[mid] < target:
                left = mid + 1
            else:
                return True
        
        return False
         