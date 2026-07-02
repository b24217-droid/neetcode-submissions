# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # IN PLACE
        # reverse 
        # remove node 
        # reverse again
        if not head:
            return None
        if n == 1:
            curr = head
            while curr.next and curr.next.next:
                curr = curr.next
            if not curr.next:
                return None
            curr.next = curr.next.next
            return head
    
        head , count_nodes = self.reverse(head)
        curr = head
        while n > 2 :
            curr = curr.next
            n -= 1
        

        curr.next = curr.next.next
        head , _ = self.reverse(head)
        return head
        

        

    def reverse(self, head):
        if not head:
            return None , 0
        curr = head
        prev = None
        count = 0
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        return prev , count
