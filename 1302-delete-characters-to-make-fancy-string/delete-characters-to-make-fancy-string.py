class Solution(object):
    def makeFancyString(self, s):
        res = []
        count=1

        for i in range(1, len(s)):
            if s[i] ==s[i-1]:
                count +=1
            else:
                count=1

            if count<3:
                res.append(s[i-1])
        res.append(s[-1])
        return ''.join(res)