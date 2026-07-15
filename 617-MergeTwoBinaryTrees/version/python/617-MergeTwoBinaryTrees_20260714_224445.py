# Last updated: 7/14/2026, 10:44:45 PM
# Always use recursion to build trees for height balanced BST
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
9        # Base case: if the slice of the array is empty, return None
10        if not nums:
11            return None
12        
13        # Find the middle index
14        mid = len(nums) // 2
15        
16        # Create the root node with the middle element
17        root = TreeNode(nums[mid])
18        
19        # Recursively build the left and right subtrees
20        root.left = self.sortedArrayToBST(nums[:mid])
21        root.right = self.sortedArrayToBST(nums[mid+1:])
22        
23        return root
24