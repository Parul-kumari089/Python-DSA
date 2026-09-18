class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr != None:
            if curr.next != None and curr.val == curr.next.val:
                duplicate = curr.val

                while curr != None and curr.val == duplicate:
                    curr = curr.next

                prev.next = curr

            else:
                prev = curr
                curr = curr.next

        return dummy.next