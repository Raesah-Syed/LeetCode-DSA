# Last updated: 6/20/2026, 7:58:20 PM
# Without a dummy LL
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
8        while head and head.val==val:
9            head=head.next
10
11        if not head:
12            return None
13        
14        temp=head
15
16        while temp:
17
18            if temp.next and temp.next.val==val:
19                temp.next=temp.next.next
20            else:
21                temp=temp.next
22        
23        return head
24