# Last updated: 7/12/2026, 5:20:20 PM
# split the problem into smaller tasks
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        
10        def tr(node,r):
11            if not node:
12                return
13            
14            if not node.left and not node.right:
15                r.append(node.val)
16            
17            tr(node.left,r)
18            tr(node.right,r)
19        r1=[]
20        r2=[]
21        tr(root1,r1)
22        tr(root2,r2)
23
24        return r1==r2
25
26   
27
28        