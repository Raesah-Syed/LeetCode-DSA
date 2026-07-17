# Last updated: 7/16/2026, 11:13:52 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
9        self.x=0
10        def tr(node):
11            
12            if not node:
13                return 0
14
15            if node.left and not node.left.right and not node.left.left:
16                self.x+=node.left.val 
17            
18            tr(node.left)
19            tr(node.right)
20
21        tr(root)
22        return self.x
23
24
25
26