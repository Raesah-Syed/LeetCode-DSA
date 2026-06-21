# Last updated: 6/20/2026, 7:39:57 PM
# Always store the node object itself, not its value. Nodes are unique references; values are just integers that can repeat. Using a set instead of a list keeps your lookup time at O(1)
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