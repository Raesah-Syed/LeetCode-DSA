# Last updated: 7/11/2026, 6:27:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def checkTree(self, root: Optional[TreeNode]) -> bool:
9        return root.left.val+root.right.val==root.val