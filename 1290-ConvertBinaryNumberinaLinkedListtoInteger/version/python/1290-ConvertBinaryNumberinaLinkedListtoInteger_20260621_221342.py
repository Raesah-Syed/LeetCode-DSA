# Last updated: 6/21/2026, 10:13:42 PM
# Break the problem into multiple steps and code accordingly
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if not head:
13            return None
14
15        #Create Clone of nodes right beside each other without links to random
16        curr=head
17        while curr:
18            new_node=Node(curr.val)
19            new_node.next=curr.next
20            curr.next=new_node
21            curr=new_node.next
22
23        #Link the random nodes of each cloned node referring the original node's random
24        curr=head
25        while curr:
26            if curr.random:
27                curr.next.random=curr.random.next
28            curr=curr.next.next
29        
30        curr=head
31        new_head=head.next
32        copy_curr=new_head
33
34        while curr:
35            curr.next=curr.next.next
36            if copy_curr.next:
37                copy_curr.next=copy_curr.next.next
38            
39            curr=curr.next
40            copy_curr=copy_curr.next
41        
42        return new_head
43        