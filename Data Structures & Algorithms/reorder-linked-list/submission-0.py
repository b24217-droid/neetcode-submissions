# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #  find the middle 
        # divide them 
        # reverse the second half
        # merge them IN PLACE

        slow , fast = head  , head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None

        # reverse the second half
        curr = head2
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node

        first , second = head , prev

        while second: # because by definition second will be shorter
            next_nodes1 = first.next
            next_nodes2 = second.next

            first.next = second
            second.next = next_nodes1
            first = next_nodes1
            second = next_nodes2


        

