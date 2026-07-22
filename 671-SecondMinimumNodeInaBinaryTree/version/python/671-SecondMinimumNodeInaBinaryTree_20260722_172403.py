# Last updated: 7/22/2026, 5:24:03 PM
1class Solution:
2    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
3        self.ans = float('inf')
4        min_val = root.val
5
6        def dfs(node):
7            if not node:
8                return
9            
10            # Found a value larger than min_val
11            if node.val > min_val:
12                self.ans = min(self.ans, node.val)
13                return  # PRUNE: Do not traverse node.left or node.right
14            
15            # Value equals min_val, keep searching deeper
16            dfs(node.left)
17            dfs(node.right)
18
19        dfs(root)
20        return self.ans if self.ans != float('inf') else -1