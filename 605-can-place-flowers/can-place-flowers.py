class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n ==0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]== 0) and (i== len(flowerbed)-1 or flowerbed[i+1] ==0):
                n-=1
                if n ==0: return True
                flowerbed[i] =1
        return False

            
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        