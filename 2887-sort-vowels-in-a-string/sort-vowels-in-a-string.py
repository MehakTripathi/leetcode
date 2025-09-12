class Solution:
    def sortVowels(self, s: str) -> str:
        t= list(s)
        l1=[]

        for i in t:
            if i in "AEIOUaeiou":
                l1.append(i)

        if l1 ==[]:
            return s

        l1.sort()
        count=0
        for j in range(len(s)):
            if t[j] in "AEIOUaeiou":
                t[j] = l1[count]
                count +=1
        return ''.join(t)
