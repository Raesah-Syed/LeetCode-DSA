# Last updated: 6/20/2026, 6:26:27 PM
# Use a dummy node to create the new merged node
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        dummy=ListNode(-1)
10        tail=dummy
11
12        while list1 and list2:
13            if list1.val<=list2.val:
14                tail.next=list1
15                list1=list1.next
16            
17            else:
18                tail.next=list2
19                list2=list2.next
20            tail=tail.next
21
22        tail.next=list1 if list1 else list2
23
24    
25        return dummy.next
26        
27
28
29