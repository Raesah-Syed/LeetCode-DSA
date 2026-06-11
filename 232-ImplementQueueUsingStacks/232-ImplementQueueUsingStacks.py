# Last updated: 6/10/2026, 11:43:03 PM
class MyQueue:

    def __init__(self):
        self.s1 = []  # For incoming elements (push)
        self.s2 = []  # For outgoing elements (pop/peek)

    def push(self, x: int) -> None:
        # Just push straight to s1. Very simple, O(1) time.
        self.s1.append(x)

    def pop(self) -> int:
        # If s2 is empty, move EVERYTHING from s1 over to s2 to reverse the order
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # Now the front of the queue is cleanly sitting at the top of s2
        return self.s2.pop()

    def peek(self) -> int:
        # Same logic as pop: fill s2 if it's empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # Just look at the top item without removing it
        return self.s2[-1]

    def empty(self) -> bool:
        # The queue is only empty if BOTH stacks are empty
        return len(self.s1) == 0 and len(self.s2) == 0