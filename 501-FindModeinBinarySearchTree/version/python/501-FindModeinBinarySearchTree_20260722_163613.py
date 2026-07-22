# Last updated: 7/22/2026, 4:36:13 PM
1class Solution:
2    def findMode(self, root: Optional[TreeNode]) -> List[int]:
3        self.curr_val = None
4        self.curr_count = 0
5        self.max_count = 0
6        self.modes = []
7
8        def inorder(node):
9            if not node:
10                return
11
12            inorder(node.left)
13
14            # Process current node
15            if node.val == self.curr_val:
16                self.curr_count += 1
17            else:
18                self.curr_val = node.val
19                self.curr_count = 1
20
21            # Update modes list dynamically
22            if self.curr_count > self.max_count:
23                self.max_count = self.curr_count
24                self.modes = [node.val]
25            elif self.curr_count == self.max_count:
26                self.modes.append(node.val)
27
28            inorder(node.right)
29
30        inorder(root)
31        return self.modes