class Solution(object):
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i] == needle[0]:
                for j in range(n):
                    if haystack[i + j] != needle[j]:
                        break
                else:
                    return i
        return -1
                
      
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        