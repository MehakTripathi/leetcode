class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        a= x
        if x<0:
            pass
        else:
            rev = int(str(x)[::-1])
              
        
        if a== rev:
            return True
        else:
            return False
        