class Solution(object):
    def isPalindrome(self, s):
        n= len(s)
        s1=""
        s2=""
        for i in range(n):
            if (s[i].isalnum()==True):
                s1+=s[i]
        for i in range(n-1,-1,-1):
            if (s[i].isalnum()==True):
                s2+=s[i]
        s1=s1.lower()
        s2=s2.lower()
        if s1==s2:
            return True
        else:
            return False
               