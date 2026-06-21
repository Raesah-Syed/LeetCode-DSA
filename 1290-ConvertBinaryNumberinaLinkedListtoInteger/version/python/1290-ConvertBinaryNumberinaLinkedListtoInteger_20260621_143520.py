# Last updated: 6/21/2026, 2:35:20 PM
# Optimal solution with O(1) memory
1class Solution:
2    def reorderList(self, head: Optional[ListNode]) -> None:
3        """
4        Do not return anything, modify head in-place instead.
5        """
6        if not head or not head.next:
7            return
8        
9        # Step 1: Find the middle of the linked list
10        slow = head
11        fast = head
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15            
16        # Step 2: Reverse the second half in-place
17        # prev will be the head of the reversed second half
18        prev = None
19        curr = slow.next
20        slow.next = None  # Cut the first half from the second half
21        
22        while curr:
23            nxt = curr.next
24            curr.next = prev
25            prev = curr
26            curr = nxt
27            
28        # Step 3: Interleave the two halves
29        first = head
30        second = prev  # The reversed second half head
31        
32        while second:
33            nxt1 = first.next
34            nxt2 = second.next
35            
36            first.next = second
37            second.next = nxt1
38            
39            first = nxt1
40            second = nxt2