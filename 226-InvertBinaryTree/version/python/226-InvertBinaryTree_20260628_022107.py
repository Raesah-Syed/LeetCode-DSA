# Last updated: 6/28/2026, 2:21:07 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        c,m=0,-1
10        def trav(node):
11            nonlocal c,m
12            if not node:
13                if c>m:
14                    m=c
15                return
16            c+=1
17            trav(node.left)
18            trav(node.right)
19            c-=1
20
21        trav(root)
22        return m