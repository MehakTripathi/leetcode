class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        s1= list(s)
        setx = set()
        maxlen=0
        for r in range (len(s1)):
            if s1[r] in setx:
                while l<r and s1[r] in setx:
                    setx.remove(s1[l])
                    l+=1
            setx.add(s1[r])
            maxlen= max(maxlen, r-l+1)
        return maxlen

        