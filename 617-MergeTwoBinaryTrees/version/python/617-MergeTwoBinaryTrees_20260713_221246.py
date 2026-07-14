# Last updated: 7/13/2026, 10:12:46 PM
# TRaverse according to the root value because this is a BST
1class Solution:
2    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
3        self.s = 0
4        
5        def tr(node):
6            if not node:
7                return
8            
9            # If current value is within range, add it
10            if low <= node.val <= high:
11                self.s += node.val
12            
13            # ONLY go left if there's a chance left nodes are >= low
14            if node.val > low:
15                tr(node.left)
16                
17            # ONLY go right if there's a chance right nodes are <= high
18            if node.val < high:
19                tr(node.right)
20                
21        tr(root)
22        return self.s