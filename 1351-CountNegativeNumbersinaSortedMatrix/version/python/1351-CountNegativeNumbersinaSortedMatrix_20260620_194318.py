# Last updated: 6/20/2026, 7:43:18 PM
# O(1) memory
1class Solution:
2    def hasCycle(self, head: Optional[ListNode]) -> bool:
3        slow = head
4        fast = head
5        
6        # Fast moves twice as fast, so check fast and fast.next
7        while fast and fast.next:
8            slow = slow.next          # Moves 1 step
9            fast = fast.next.next     # Moves 2 steps
10            
11            if slow == fast:          # They met! Cycle detected.
12                return True
13                
14        return False