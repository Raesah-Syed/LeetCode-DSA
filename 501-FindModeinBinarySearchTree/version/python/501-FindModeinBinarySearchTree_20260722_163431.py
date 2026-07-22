# Last updated: 7/22/2026, 4:34:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findMode(self, root: Optional[TreeNode]) -> List[int]:
9        self.m={}
10        def tr(node):
11            if not node:
12                return
13            
14            tr(node.left)
15            tr(node.right)
16            self.m[node.val]=self.m.get(node.val,0)+1
17
18        tr(root)
19       
20        max_freq = max(self.m.values())
21
22        return [key for key, val in self.m.items() if val == max_freq]