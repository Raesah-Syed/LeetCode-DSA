# Last updated: 7/14/2026, 9:59:38 PM
# Since we need the minimum depth we need to consider cases where there's not left or right child otherwise we get the wrong depth
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        if not root.left:
12            return 1+self.minDepth(root.right)
13        
14        if not root.right:
15            return 1+self.minDepth(root.left)
16
17        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
18        