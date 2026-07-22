# Last updated: 7/22/2026, 3:46:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def countNodes(self, root: Optional[TreeNode]) -> int:
9        self.c=0
10        def tr(node):
11            if not node:
12                return
13            
14            self.c+=1
15            tr(node.left)
16            tr(node.right)
17
18        tr(root)
19        return self.c