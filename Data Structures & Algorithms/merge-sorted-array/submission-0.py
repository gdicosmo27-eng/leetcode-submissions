class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        L = nums1[:m]
        R = nums2
        k = m + n - 1
        j = m - 1
        i = n - 1

        while j >= 0 and i >= 0:
            if L[j] >= R[i]:
                nums1[k] = L[j]
                j -= 1
            else:
                nums1[k] = R[i]
                i -= 1
            k -= 1
        
        while k >= 0:
            if j >= 0:
                nums1[k] = L[j]
                j -= 1
            else:
                nums1[k] = R[i]
                i -= 1
            k -= 1




        