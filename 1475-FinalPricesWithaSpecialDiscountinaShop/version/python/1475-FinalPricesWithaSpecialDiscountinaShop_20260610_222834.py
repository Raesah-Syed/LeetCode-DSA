# Last updated: 6/10/2026, 10:28:34 PM
# The pop operation on a list always removes elements from the end
1class MyStack:
2
3    def __init__(self):
4        self.st=[]
5
6    def push(self, x: int) -> None:
7        self.st.append(x)
8
9    def pop(self) -> int:
10        es=self.st[-1]
11        i=0
12        del self.st[-1]
13        return es
14
15    def top(self) -> int:
16        return self.st[-1]
17
18    def empty(self) -> bool:
19        return len(self.st)==0
20
21
22# Your MyStack object will be instantiated and called as such:
23# obj = MyStack()
24# obj.push(x)
25# param_2 = obj.pop()
26# param_3 = obj.top()
27# param_4 = obj.empty()