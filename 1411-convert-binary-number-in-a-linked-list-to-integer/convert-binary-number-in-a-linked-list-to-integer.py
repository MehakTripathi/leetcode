class Solution(object):
    def getDecimalValue(self, head):
      
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        
        count -= 1 
        ans = 0
        while head:
            ans += head.val * (2 ** count)
            count -= 1
            head = head.next

        return ans
