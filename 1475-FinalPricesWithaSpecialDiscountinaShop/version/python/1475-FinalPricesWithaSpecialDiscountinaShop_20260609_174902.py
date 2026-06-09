# Last updated: 6/9/2026, 5:49:02 PM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        res = []
4        depth = 0
5        
6        for char in s:
7            if char == '(':
8                # If depth > 0, this '(' is NOT an outermost parenthesis
9                if depth > 0:
10                    res.append(char)
11                depth += 1
12            else:
13                # If depth > 1, this ')' is NOT an outermost parenthesis
14                depth -= 1
15                if depth > 0:
16                    res.append(char)
17                    
18        return "".join(res)