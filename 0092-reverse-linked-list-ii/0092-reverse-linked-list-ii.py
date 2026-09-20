# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if head == None or left == right:
            return head 
        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy
        for i in range(left-1):
            prev= prev.next
        curr= prev.next 
        for i in range(right - left):
            next_Node = curr.next
            curr.next = next_Node.next
            next_Node.next = prev.next
            prev.next = next_Node    
        return dummy.next 