# Last updated: 7/12/2026, 4:40:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root1:
10            return root2
11        if not root2:
12            return root1
13        
14        m=TreeNode(root1.val+root2.val)
15
16        m.left=self.mergeTrees(root1.left,root2.left)
17        m.right=self.mergeTrees(root1.right,root2.right)
18
19        return m