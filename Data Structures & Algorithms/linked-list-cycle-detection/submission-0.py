# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 0 or 1 element lists
        if head is None or head.next is None:
            return False

        # 2+
        slow = head
        fast = head
        while fast and fast.next: # Are not none
            slow = slow.next
            fast = fast.next.next # Cycle detection algorithm
            if slow is fast:
                return True

        return False