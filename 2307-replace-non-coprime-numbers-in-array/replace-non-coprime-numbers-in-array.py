class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s=[]
        for num in nums:
            while s and math.gcd(s[-1], num) >1:
                top= s.pop()
                num=(top * num)//math.gcd(top,num)
            s.append(num)
        return s
        