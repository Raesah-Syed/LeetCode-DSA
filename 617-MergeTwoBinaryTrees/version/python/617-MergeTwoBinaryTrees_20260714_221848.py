# Last updated: 7/14/2026, 10:18:48 PM
# Use shift and add logic of binary numbers to get through the problem
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
10        
11        def tr(node, current_val):
12            # Base case: if we hit a null node, return 0
13            if not node:
14                return 0
15            
16            # Step 1: "Shift and Add" to update our binary value
17            current_val = (current_val * 2) + node.val
18            
19            # Step 2: If we reached a leaf node, return the final calculated value
20            if not node.left and not node.right:
21                return current_val
22            
23            # Step 3: Otherwise, recurse down both branches and return their sum
24            return tr(node.left, current_val) + tr(node.right, current_val)
25        
26        # Start the recursion from the root with an initial value of 0
27        return tr(root, 0)