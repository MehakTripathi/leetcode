# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy 
        carry = 0

        while l1 or l2 or carry:
            sum = carry 
            if l1:
                sum +=l1.val
                l1= l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr= curr.next
        return dummy.next
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        