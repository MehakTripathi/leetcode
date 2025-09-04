class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []

        for i in num:
            while k > 0 and s and s[-1] > i:
                k -= 1
                s.pop()
            s.append(i)
        s = s[:len(s) - k]
        res = "".join(s).lstrip("0")  
        return res if res else "0"
