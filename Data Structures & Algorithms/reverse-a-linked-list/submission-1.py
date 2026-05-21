# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # 1 - > 2 - > 3
       # None <- 1 < - 2 < - 3
        prev = None
        current = head
        while current:
            new = current.next
            current.next = prev
            prev = current
            current = new
        return prev

        

        




        

        