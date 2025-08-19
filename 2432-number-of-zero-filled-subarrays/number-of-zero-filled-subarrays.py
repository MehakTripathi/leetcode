class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, s= 0,0
        for i in nums:
            if i ==0:
                s+=1
                count += s
            else:
                s =0
        return count


        