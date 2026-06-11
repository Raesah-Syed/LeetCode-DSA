# Last updated: 6/10/2026, 10:40:40 PM
# This is the right queue implementation of stack
1class MyStack:
2
3    def __init__(self):
4        self.q=deque()
5
6    def push(self, x: int) -> None:
7        self.q.append(x)
8
9        for _ in range(len(self.q)-1):
10            old_element=self.q.popleft()
11            self.q.append(old_element)
12
13    def pop(self) -> int:
14        return self.q.popleft()
15
16    def top(self) -> int:
17        return self.q[0]
18
19    def empty(self) -> bool:
20        return len(self.q)==0
21
22
23# Your MyStack object will be instantiated and called as such:
24# obj = MyStack()
25# obj.push(x)
26# param_2 = obj.pop()
27# param_3 = obj.top()
28# param_4 = obj.empty()