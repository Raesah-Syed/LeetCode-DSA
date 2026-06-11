# Last updated: 6/10/2026, 11:42:46 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        
        for char in s:
            if char == '(':
                # If depth > 0, this '(' is NOT an outermost parenthesis
                if depth > 0:
                    res.append(char)
                depth += 1
            else:
                # If depth > 1, this ')' is NOT an outermost parenthesis
                depth -= 1
                if depth > 0:
                    res.append(char)
                    
        return "".join(res)