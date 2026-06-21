# Last updated: 6/20/2026, 7:39:37 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        s=[]
10        temp=head
11        while temp:
12            if temp not in s:
13                s.append(temp)
14            else:
15                
16                return True
17            temp=temp.next
18        return False