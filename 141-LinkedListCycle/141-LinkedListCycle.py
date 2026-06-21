# Last updated: 6/20/2026, 11:50:13 PM
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # Fast moves twice as fast, so check fast and fast.next
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            if slow == fast:          # They met! Cycle detected.
                return True
                
        return False