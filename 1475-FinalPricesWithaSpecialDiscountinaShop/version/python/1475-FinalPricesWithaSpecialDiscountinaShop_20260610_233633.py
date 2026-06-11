# Last updated: 6/10/2026, 11:36:33 PM
1class MinStack:
2
3    def __init__(self):
4        self.s1=[]
5        self.s2=[]
6
7    def push(self, value: int) -> None:
8        self.s1.append(value)
9        if not self.s2:
10            self.s2.append(value)
11        else:
12            if self.s2[-1]<value:
13                self.s2.append(self.s2[-1])
14            else:
15                self.s2.append(value)
16    def pop(self) -> None:
17        
18        del self.s1[-1]
19        del self.s2[-1]
20
21
22    def top(self) -> int:
23        return self.s1[-1]
24
25    def getMin(self) -> int:
26        if self.s2:
27            return (self.s2[-1])
28        else:
29            return []
30        
31
32
33# Your MinStack object will be instantiated and called as such:
34# obj = MinStack()
35# obj.push(value)
36# obj.pop()
37# param_3 = obj.top()
38# param_4 = obj.getMin()