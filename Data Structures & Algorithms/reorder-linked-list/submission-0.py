# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Recall the core operations of a linked list
        # 
        # Count how many elements are in the linked list

        # Maybe we need to determine the length of the linked list first?
        # Maybe we also need to find a way to count t

        # WE might need an neet code explanation for this one

        # The trick we need to understand linked lists a little better was an initial linked list algorithm called the Fast and Slow Pointers
        # fast, slow = head, head
        # while fast and fast.next: # This ends here
        #     print(slow.val)
        #     print(fast.val)
        #     slow = slow.next
        #     fast = fast.next.next

            
        # With this problem we need to find the middle
        # Then we need to reverse the second half linked list
        # Then we need to merge the two lists together
        slow, fast = head, head.next # This handles all situations of linked list
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        second_list = slow.next
        slow.next = None # Make sure these are separated into 3 lists
        prev = None

        # Reverse the linked list 
        while second_list:
            tmp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = tmp

        first = head
        second = prev

        while second:
            # We need a better understanding of the merging of 2 linked lists
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2





