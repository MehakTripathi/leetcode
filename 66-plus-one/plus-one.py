class Solution(object):
    def plusOne(self, digits):
        ans=""
        rer=0
        for i in digits:
            ans+=str(i)
        rer= int(ans) +1

        return [int(ch) for ch in str(rer)]
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        