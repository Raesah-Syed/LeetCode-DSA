# Last updated: 6/21/2026, 1:53:14 PM
1class Solution:
2    def reorderList(self, head: Optional[ListNode]) -> None:
3        """
4        Do not return anything, modify head in-place instead.
5        """
6        if not head or not head.next:
7            return None
8        
9        slow=head
10        fast=head
11
12        while fast and fast.next:
13            slow=slow.next
14            fast=fast.next.next
15
16        s=[]
17        curr=slow.next
18        slow.next=None
19        while curr:
20            s.append(curr)
21            curr=curr.next
22       
23        temp=head
24
25        while s:
26            x=s.pop()
27
28            nxt=temp.next
29            temp.next=x
30            x.next=nxt
31
32            temp=nxt
33            
34    
35        
36    
37        
38        
39
40
41         