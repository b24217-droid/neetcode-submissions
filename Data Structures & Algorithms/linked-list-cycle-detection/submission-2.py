# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if not head:
            return False


        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False
    