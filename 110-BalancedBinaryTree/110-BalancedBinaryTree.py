# Last updated: 5/14/2026, 9:16:16 AM
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_height(node):
            if not node:
                return 0
            
            # --- THE LEFT SIDE CHECK ---
            left_h = check_height(node.left)
            if left_h == -1: # If alarm was rung below, keep it ringing!
                return -1
            
            # --- THE RIGHT SIDE CHECK ---
            right_h = check_height(node.right)
            if right_h == -1: # If alarm was rung below, keep it ringing!
                return -1
            
            # --- THE BALANCE TEST ---
            # Using our example: Node 1 sees left_h=2 and right_h=0
            if abs(left_h - right_h) > 1:
                return -1 # Returns -1 because 2 - 0 = 2
            
            # If healthy, send height up: 1 + tallest child
            return max(left_h, right_h) + 1

        # The final answer: Was the result -1? 
        # In our example, result is -1, so this returns False.
        return check_height(root) != -1