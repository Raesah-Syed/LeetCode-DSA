# Last updated: 6/10/2026, 10:56:59 PM
1class MyQueue:
2
3    def __init__(self):
4        self.s1 = []  # For incoming elements (push)
5        self.s2 = []  # For outgoing elements (pop/peek)
6
7    def push(self, x: int) -> None:
8        # Just push straight to s1. Very simple, O(1) time.
9        self.s1.append(x)
10
11    def pop(self) -> int:
12        # If s2 is empty, move EVERYTHING from s1 over to s2 to reverse the order
13        if not self.s2:
14            while self.s1:
15                self.s2.append(self.s1.pop())
16        # Now the front of the queue is cleanly sitting at the top of s2
17        return self.s2.pop()
18
19    def peek(self) -> int:
20        # Same logic as pop: fill s2 if it's empty
21        if not self.s2:
22            while self.s1:
23                self.s2.append(self.s1.pop())
24        # Just look at the top item without removing it
25        return self.s2[-1]
26
27    def empty(self) -> bool:
28        # The queue is only empty if BOTH stacks are empty
29        return len(self.s1) == 0 and len(self.s2) == 0