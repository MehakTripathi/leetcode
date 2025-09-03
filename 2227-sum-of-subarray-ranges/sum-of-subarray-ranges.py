class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def fn(op):

            n=len(nums)
            total=0
            s=[]

            for i in range(n+1):
                while s and (i== n or op(nums[s[-1]], nums[i])):
                    mid= s.pop()
                    m=s[-1] if s else -1
                    total += nums[mid] * (i-mid) *(mid-m)
                s.append(i)
            return total

        return fn(lt) - fn(gt)


       