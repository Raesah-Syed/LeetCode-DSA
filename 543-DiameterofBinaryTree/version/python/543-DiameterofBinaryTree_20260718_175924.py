# Last updated: 7/18/2026, 5:59:24 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        self.sd=-1
10        def depth(node):
11            if not node:
12                return 0
13            
14            sl=depth(node.left)
15            sr=depth(node.right)
16
17            self.sd=max(self.sd,sl+sr)
18            return 1+max(sl,sr)
19        depth(root)
20        return self.sd
21
22