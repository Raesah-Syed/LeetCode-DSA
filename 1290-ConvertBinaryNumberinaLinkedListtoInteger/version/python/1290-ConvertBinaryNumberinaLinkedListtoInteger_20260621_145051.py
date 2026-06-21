# Last updated: 6/21/2026, 2:50:51 PM
# Use a gap of n between slow and fast pointers to get the nth element from end (pointed by slow)
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
9        # 1. Create a dummy node to handle edge cases easily (like removing the head)
10        dummy = ListNode(0, head)
11        fast = dummy
12        slow = dummy
13        
14        # 2. Advance the 'fast' pointer forward by n + 1 steps.
15        # We do n + 1 steps so that 'slow' stops exactly BEFORE the target node.
16        for _ in range(n + 1):
17            fast = fast.next
18            
19        # 3. Move both pointers together at the same speed until 'fast' reaches the end.
20        while fast:
21            slow = slow.next
22            fast = fast.next
23            
24        # 4. 'slow' is now right before the target node. Skip the target node to delete it.
25        slow.next = slow.next.next
26        
27        # 5. Return the actual head of the modified list
28        return dummy.next