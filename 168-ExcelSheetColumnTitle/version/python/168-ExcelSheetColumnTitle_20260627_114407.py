# Last updated: 6/27/2026, 11:44:07 AM
# Pre-order (Node-> Left-> Right)
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res=[]
10        def traverse(node):
11            if not node:
12                return
13            
14            res.append(node.val)
15            traverse(node.left)
16            traverse(node.right)
17        
18        traverse(root)
19        return res