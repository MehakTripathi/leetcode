class Solution(object):
    def lengthOfLastWord(self, s):
        strings= s.split()
        return len(strings[-1])
        """
        :type s: str
        :rtype: int
        """
        