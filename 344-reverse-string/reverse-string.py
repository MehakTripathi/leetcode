class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        