# Last updated: 7/22/2026, 3:29:31 PM
# Compare the right children left.left with right.right and left.right with right.left
1class Solution:
2    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
3        if not root:
4            return True
5
6        def tr(left, right):
7            if not left and not right:
8                return True
9            if not left or not right:
10                return False
11
12            return (left.val == right.val) and \
13                   tr(left.left, right.right) and \
14                   tr(left.right, right.left)
15
16        return tr(root.left, root.right)