# Last updated: 5/17/2026, 10:10:59 PM
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Tweak 1: Pre-allocate list of size n so outputs remain in order (0 to n-1)
        res = [0] * n
        stack = []
        
        while len(logs) > 0:
            # Keep your strategy of reading from the back
            x = logs.pop()
            
            # Tweak 2: Fix splitting to safely capture multi-digit numbers/strings
            parts = x.split(':')
            pid = int(parts[0])
            stp = parts[1]
            pt = int(parts[2])

            if stp == 'end':
                # An 'end' log means this function was running. 
                # Save its ID and its end timestamp onto our tracking stack.
                stack.append((pid, pt))
            else:
                # A 'start' log matches the last recorded 'end' log on the stack
                popped_id, end_time = stack.pop()
                
                # Calculate raw duration inclusive of boundaries (+1)
                duration = end_time - pt + 1
                
                # Tweak 3: Deduct this runtime from the parent function holding it
                res[pid] += duration
                if stack:
                    parent_id = stack[-1][0]
                    res[parent_id] -= duration
                    
        return res