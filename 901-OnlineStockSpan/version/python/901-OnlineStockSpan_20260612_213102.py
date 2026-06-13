# Last updated: 6/12/2026, 9:31:02 PM
# Use the stack to store lists which act as log and help count span incrementally instead of from scratch
1class StockSpanner:
2
3    def __init__(self):
4        self.st=[]
5
6
7    def next(self, price: int) -> int:
8        c=1
9        while self.st and self.st[-1][0]<=price:
10            x=self.st.pop()
11            c+=x[1]
12            
13        
14        self.st.append([price,c])
15
16        return c