# Last updated: 6/20/2026, 6:03:31 PM
# Don't forget to return the new head which is before
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9        temp=head
10        before=None
11        
12        while temp:
13            after=temp.next
14            temp.next=before
15            before=temp
16            temp=after
17    
18        return before
19
20        
21