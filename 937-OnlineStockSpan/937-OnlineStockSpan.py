# Last updated: 6/14/2026, 11:43:38 PM
class StockSpanner:

    def __init__(self):
        self.st=[]


    def next(self, price: int) -> int:
        c=1
        while self.st and self.st[-1][0]<=price:
            x=self.st.pop()
            c+=x[1]
            
        
        self.st.append([price,c])

        return c