class Solution(object):
    def reverseWords(self, s):
        s =s.split()
        s= s[::-1]
        return ' '.join(s)
        
        
        
        """
        :type s: str
        :rtype: str
        """
        