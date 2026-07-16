# Last updated: 7/15/2026, 11:04:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        def tr(node,s):
10            if not node:
11                return False
12            
13            x=s+node.val
14
15            if not node.left and not node.right:
16                return x==targetSum
17            
18            return tr(node.left,x) or tr(node.right,x)
19        if root:
20           return tr(root,0)
21        return False
22        
23        