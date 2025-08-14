class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1): 
            triplet = str(i) * 3    
            if triplet in num:
                return triplet
        return ""
            




        