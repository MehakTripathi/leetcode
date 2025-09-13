class Solution:
    def maxFreqSum(self, s: str) -> int:
        c,v =0,0
        myset= set(s)
        for i in myset:
            if i in "aeiou":
                v= max(v, s.count(i))
            else:
                c= max(c, s.count(i))
        return c+v
        