# Last updated: 6/20/2026, 8:01:16 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
8        dummy=ListNode(-1)
9        dummy.next=head
10        current=dummy
11
12        while current.next:
13
14            if current.next.val==val:
15                current.next=current.next.next
16            else:
17                current=current.next
18        
19        return dummy.next
20            