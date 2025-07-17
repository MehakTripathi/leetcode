class Solution(object):
    def romanToInt(self, s):
        n= len(s)
        mymap={'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000 }
        ans= 0
        for i in range(n):
            if i< n-1 and mymap[s[i]] < mymap[s[i+1]]:
                ans -= mymap[s[i]]
            else:
                ans += mymap[s[i]]
        return ans
        """
        :type s: str
        :rtype: int
        """
        