# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, start,end):
        prev, curr = None, start 
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseKGroup(self, head, k):
        count, temp =0, head
        while temp and count<k:
            temp = temp.next
            count +=1
        if count <k:
            return head
            

        newHead =self.reverse(head,temp)
        head.next = self.reverseKGroup(temp, k)
        return newHead

        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        