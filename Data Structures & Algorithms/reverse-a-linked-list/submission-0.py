# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = ListNode()
        while head:
            node = ListNode(val=head.val, next=reversed.next)
            reversed.next = node
            head = head.next
        return reversed.next