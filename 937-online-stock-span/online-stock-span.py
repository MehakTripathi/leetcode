class StockSpanner(object):

    def __init__(self):
        self.stack=[]

    def next(self, price):
        span= 1
        while self.stack and self.stack[-1][0]<= price:
            span+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,span))
        return span
        """
        :type price: int
        :rtype: int
        """
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)