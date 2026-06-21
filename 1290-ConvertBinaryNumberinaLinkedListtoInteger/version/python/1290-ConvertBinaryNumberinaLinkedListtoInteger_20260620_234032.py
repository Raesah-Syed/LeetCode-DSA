# Last updated: 6/20/2026, 11:40:32 PM
# Tortoise and Hare or Floyd's Cycle-Finding Algo
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        slow,fast=head,head
9
10        while fast and fast.next:
11            slow=slow.next
12            fast=fast.next.next
13        
14        return(slow)