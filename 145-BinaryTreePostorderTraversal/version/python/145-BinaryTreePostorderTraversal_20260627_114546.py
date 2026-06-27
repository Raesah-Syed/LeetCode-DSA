# Last updated: 6/27/2026, 11:45:46 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        r=[]
10        def traverse(node):
11            if not node:
12                return
13            
14            traverse(node.left)
15            traverse(node.right)
16            r.append(node.val)
17        traverse(root)
18        return r