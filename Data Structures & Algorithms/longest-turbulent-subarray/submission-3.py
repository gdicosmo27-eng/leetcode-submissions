class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        R = 2
        if len(arr) == 1:
            return 1

        if arr[0] != arr[1]:
            curLength = maxLength = 2 
        else:
            curLenght = maxLength = 1

        while R < len(arr):
            if (arr[R] - arr[R - 1]) * (arr[R - 1] - arr[R - 2]) < 0:
                R += 1
                curLength += 1
            elif arr[R] != arr[R - 1]:
                curLength = 2
                R += 1
            else:
                curLength = 1
                R += 1
            
            maxLength = max(maxLength, curLength)
            

        return maxLength