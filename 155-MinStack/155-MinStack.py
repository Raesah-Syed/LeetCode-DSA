# Last updated: 6/10/2026, 11:43:46 PM
class MinStack:

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, value: int) -> None:
        self.s1.append(value)
        if not self.s2:
            self.s2.append(value)
        else:
            if self.s2[-1]<value:
                self.s2.append(self.s2[-1])
            else:
                self.s2.append(value)
    def pop(self) -> None:
        
        del self.s1[-1]
        del self.s2[-1]


    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        if self.s2:
            return (self.s2[-1])
        else:
            return []
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()