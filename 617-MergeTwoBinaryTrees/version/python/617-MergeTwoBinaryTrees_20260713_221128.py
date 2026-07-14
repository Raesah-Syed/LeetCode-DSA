# Last updated: 7/13/2026, 10:11:28 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
9        self.s=0
10        def tr(node):
11            if not node:
12                return
13            
14            tr(node.left)
15            tr(node.right)
16
17            if node.val>=low and node.val<=high:
18                self.s+=node.val
19        
20        tr(root)
21        return self.s