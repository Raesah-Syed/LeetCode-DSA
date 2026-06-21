# Last updated: 6/20/2026, 11:50:17 PM
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current =head

        while current and current.next:

            if current.val==current.next.val:
                current.next=current.next.next
            else:
                current=current.next


        return head
        
