# Last updated: 7/15/2026, 10:38:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
9        r=[]
10        def tr(node,curr):
11            if not node:
12                return 0
13            
14            if curr:
15                new=curr+"->"+str(node.val)
16            else:
17                new=str(node.val)
18            
19            if not node.left and not node.right:
20                r.append(new)
21                return
22            
23            tr(node.left,new)
24            tr(node.right,new)
25        
26        tr(root, "")
27        return r