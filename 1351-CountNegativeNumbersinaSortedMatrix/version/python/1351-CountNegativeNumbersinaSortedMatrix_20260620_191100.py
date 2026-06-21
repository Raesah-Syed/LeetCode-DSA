# Last updated: 6/20/2026, 7:11:00 PM
1class Solution:
2    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        
4        current =head
5
6        while current and current.next:
7
8            if current.val==current.next.val:
9                current.next=current.next.next
10            else:
11                current=current.next
12
13
14        return head
15        
16