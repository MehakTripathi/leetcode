class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]



        """
        :type a: str
        :type b: str
        :rtype: str
        """
        