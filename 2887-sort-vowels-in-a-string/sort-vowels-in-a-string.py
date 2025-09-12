class Solution:
    def sortVowels(self, s: str) -> str:
        '''t= list(s)
        l1=[]

        for i in t:
            if i in "AEIOUaeiou":
                l1.append(i)

        if l1 ==[]:
            return s
                                          [***BRUTE FORCE***]
        l1.sort()
        count=0
        for j in range(len(s)):
            if t[j] in "AEIOUaeiou":
                t[j] = l1[count]
                count +=1
        return ''.join(t)'''

        vset= set("AEIOUaeiou")
        v= [i for i in s if i in vset]
        v.sort()
        res=[]                                #OPTIMIZED SOL.N      
        l1= iter(v)

        for i in s:
            res.append(next(l1) if i in vset else i)

        return ''.join(res)
