# Last updated: 6/22/2026, 9:48:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy=ListNode(0)
9        current=dummy
10        c=0
11
12        h1=l1
13        h2=l2
14                
15        while h1 or h2 or c:
16            val1=h1.val if h1 else 0
17            val2=h2.val if h2 else 0
18
19            ts=val1+val2+c
20            c=ts//10
21            digit=ts%10
22
23            current.next=ListNode(digit)
24            current=current.next
25
26            if h1: h1=h1.next
27            if h2: h2=h2.next
28        
29        return dummy.next
30
31
32            