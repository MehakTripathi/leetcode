class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res= [0]* len(temp)
        s=[]

        for i, t in enumerate(temp):
            while s and t> s[-1][0]:
                sT, sInd = s.pop()
                res[sInd]= (i-sInd)
            s.append([t, i])
        return res

        