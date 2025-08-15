class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n= len(nums1)
        mymap= {n: i for i, n in enumerate(nums1)}
        res=[-1]*n
        st=[]

        for i in range(len(nums2)):
            cur= nums2[i]
            while st and cur> st[-1]:
                val=st.pop()                    # using stack
                idx= mymap[val]
                res[idx]= cur
            if cur in mymap:
                st.append(cur)
        return res


        '''n= len(nums1)
        mymap= { n: i for i, n in enumerate(nums1)}
        res= [-1]*n

        for i in range(len(nums2)):
            if nums2[i] not in mymap:
                continue                                  # BRUTE FORCE APPROACH #
            for j in range(i+1, len(nums2)):
                if nums2[j]> nums2[i]:
                    idx = mymap[nums2[i]]
                    res[idx]= nums2[j]
                    break
        return res'''

        