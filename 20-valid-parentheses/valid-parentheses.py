class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        Mymap= {')':'(', '}':'{', ']':'['}

        
        for i in s:
            if i in Mymap.values():
                stack.append(i)
            elif i in Mymap:
                if not stack or stack [-1] != Mymap[i]:
                    return False
                stack.pop()
        return len(stack) ==0

        