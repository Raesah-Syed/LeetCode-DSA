# Last updated: 7/19/2026, 4:50:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return root.val==1

        left_val=self.evaluateTree(root.left)
        right_val=self.evaluateTree(root.right)

        return left_val or right_val if root.val==2 else left_val and right_val
