# Last updated: 5/23/2026, 5:53:30 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # p1 points to the last valid element in nums1
        # p2 points to the last element in nums2
        # p_write points to the very last index of nums1
        p1, p2, p_write = m - 1, n - 1, m + n - 1
        
        # Keep going until we have placed all elements from nums2
        while p2 >= 0:
            # If nums1 still has elements AND the current p1 element is bigger
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p_write] = nums1[p1]
                p1 -= 1
            else:
                # Otherwise, take the element from nums2
                nums1[p_write] = nums2[p2]
                p2 -= 1
            # Move the writing pointer to the left
            p_write -= 1