# Last updated: 7/13/2026, 10:41:02 PM
# Use dummy and curr to navigate through the resultant tree
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        self.dummy=TreeNode(0)
10        self.curr=self.dummy
11
12        def tr(node):
13            if not node:
14                return
15            
16            tr(node.left)
17            
18            self.curr.right=TreeNode(node.val)
19            self.curr=self.curr.right
20
21            tr(node.right)
22        
23        tr(root)
24        return self.dummy.right
25