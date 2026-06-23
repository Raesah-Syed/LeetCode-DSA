# Last updated: 6/22/2026, 11:43:32 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8
9        if not head or not head.next or left==right:
10            return head
11
12        dummy=ListNode(0)
13        dummy.next=head
14        
15        left_prev=dummy
16        
17        for _ in range(left-1):
18            left_prev=left_prev.next
19        
20        curr=left_prev.next
21
22        before=None
23        temp=curr
24        x=right-left+1
25
26        while temp and x:
27            after=temp.next
28            temp.next=before
29            before=temp
30            temp=after
31            x=x-1
32
33        left_prev.next=before
34        curr.next=temp
35        
36        return dummy.next
37           
38        
39            
40
41
42