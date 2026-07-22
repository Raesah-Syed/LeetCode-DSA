# Last updated: 7/22/2026, 4:01:13 PM
1class Solution:
2    def countNodes(self, root: Optional[TreeNode]) -> int:
3        if not root:
4            return 0
5        
6        # 1. Measure left height
7        left, l_depth = root, 0
8        while left:
9            l_depth += 1
10            left = left.left
11            
12        # 2. Measure right height
13        right, r_depth = root, 0
14        while right:
15            r_depth += 1
16            right = right.right
17            
18        # 3. If perfect binary tree, return 2^h - 1
19        if l_depth == r_depth:
20            return (1 << l_depth) - 1
21            
22        # 4. Otherwise recurse: 1 (root) + left subtree + right subtree
23        return 1 + self.countNodes(root.left) + self.countNodes(root.right)