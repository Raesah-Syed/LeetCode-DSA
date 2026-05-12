# Last updated: 5/12/2026, 1:35:56 PM
1class Solution:
2    def isBalanced(self, root: Optional[TreeNode]) -> bool:
3        
4        def check_height(node):
5            if not node:
6                return 0
7            
8            # --- THE LEFT SIDE CHECK ---
9            left_h = check_height(node.left)
10            if left_h == -1: # If alarm was rung below, keep it ringing!
11                return -1
12            
13            # --- THE RIGHT SIDE CHECK ---
14            right_h = check_height(node.right)
15            if right_h == -1: # If alarm was rung below, keep it ringing!
16                return -1
17            
18            # --- THE BALANCE TEST ---
19            # Using our example: Node 1 sees left_h=2 and right_h=0
20            if abs(left_h - right_h) > 1:
21                return -1 # Returns -1 because 2 - 0 = 2
22            
23            # If healthy, send height up: 1 + tallest child
24            return max(left_h, right_h) + 1
25
26        # The final answer: Was the result -1? 
27        # In our example, result is -1, so this returns False.
28        return check_height(root) != -1