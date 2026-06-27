# Last updated: 6/27/2026, 11:18:54 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        result=[]
10        def traverse(node):
11            if not node:
12                return
13            
14            traverse(node.left)
15            result.append(node.val)
16            traverse(node.right)
17        
18        traverse(root)
19        return result