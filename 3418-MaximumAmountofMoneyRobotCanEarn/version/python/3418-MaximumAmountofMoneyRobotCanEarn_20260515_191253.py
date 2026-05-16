# Last updated: 5/15/2026, 7:12:53 PM
'''
sum and carry over. order maters.
O(max(N,M))
'''

1class Solution:
2    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
3        # Create a placeholder dummy node to anchor our new list
4        dummy = ListNode(0)
5        current = dummy
6        c = 0  # This is your carry
7        
8        # Keep going if l1 has digits, OR l2 has digits, OR there is a leftover carry
9        while l1 or l2 or c:
10            # Extract the values (use 0 if a list has already run out of digits)
11            val1 = l1.val if l1 else 0
12            val2 = l2.val if l2 else 0
13            
14            # Math step: Total sum for this position is val1 + val2 + any previous carry
15            total_sum = val1 + val2 + c
16            
17            # Calculate the new carry and the single digit to store
18            c = total_sum // 10
19            digit_to_store = total_sum % 10
20            
21            # Create the next node in our new list and step into it
22            current.next = ListNode(digit_to_store)
23            current = current.next
24            
25            # Move forward in the input lists if they have next nodes
26            if l1: l1 = l1.next
27            if l2: l2 = l2.next
28            
29        # The first node was just our dummy placeholder, so return the node after it
30        return dummy.next