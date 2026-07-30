# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hashmap = {}
        slow, fast = head, head
        idx = 0
        maxPair = 0

        while fast and fast.next:
            hashmap[idx] = slow.val
            idx += 1
            slow = slow.next
            fast = fast.next.next
        
        n = (2 * idx)
        while slow:
            maxPair = max(maxPair, hashmap[n - 1 -idx] + slow.val)
            idx += 1
            slow = slow.next
        
        return maxPair

        



        