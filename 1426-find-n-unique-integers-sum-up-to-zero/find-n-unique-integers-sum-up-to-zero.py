class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        p = n // 2

        for i in range(1, p+1):
            arr.append(i)
            arr.append(-i)

        if n % 2 == 1:
            arr.append(0)
            
        return arr