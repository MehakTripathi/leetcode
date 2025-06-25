# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length=0
        curr= head
        while curr:
            length+=1
            curr= curr.next
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for i in range (length-n):
            curr= curr.next
        curr.next = curr.next.next
        return dummy.next
        

       
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        