# Last updated: 5/12/2026, 12:28:05 PM
# Split the problem into smaller tasks and use recursion to perform repetitive task. Return -1 to stop the operations once there's an imbalance found
1
2class Solution:
3    def isBalanced(self, root: Optional[TreeNode]) -> bool:
4        
5        def check_height(node):
6            # 1. Base Case: If we hit a dead end, the height is 0
7            if not node:
8                return 0
9            
10            # 2. Check the Left branch
11            left_h = check_height(node.left)
12            # If the left branch is already "broken" (-1), pass the alarm up
13            if left_h == -1:
14                return -1
15            
16            # 3. Check the Right branch
17            right_h = check_height(node.right)
18            # If the right branch is already "broken" (-1), pass the alarm up
19            if right_h == -1:
20                return -1
21            
22            # 4. Check for a "Lean" at the CURRENT node
23            # If the left and right heights differ by more than 1, ring the alarm!
24            if abs(left_h - right_h) > 1:
25                return -1
26            
27            # 5. If everything is balanced, return the actual height
28            # Height is 1 (the current node) + the tallest of its children
29            return max(left_h, right_h) + 1
30
31        # Final Step: Run the helper. If it returns -1, the tree is unbalanced (False).
32        # If it returns a height (0 or higher), the tree is balanced (True).
33        return check_height(root) != -1