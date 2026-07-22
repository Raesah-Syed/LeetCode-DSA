# Last updated: 7/22/2026, 4:56:17 PM
1class Solution:
2    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
3        vals = set()
4
5        def tr(node):
6            if not node:
7                return
8            vals.add(node.val)
9            tr(node.left)
10            tr(node.right)
11
12        tr(root)
13
14        sorted_vals = sorted(vals)
15        return sorted_vals[1] if len(sorted_vals) > 1 else -1