# Last updated: 7/12/2026, 4:40:04 PM
1class Solution:
2    def maxDepth(self, root: 'Node') -> int:
3        if not root:
4            return 0
5        
6        # Use a queue to process the tree level by level
7        queue = [root]
8        depth = 0
9        
10        while queue:
11            # Increment depth for each level we process
12            depth += 1
13            level_size = len(queue)
14            
15            # Process all nodes currently at this level
16            for _ in range(level_size):
17                current_node = queue.pop(0)
18                
19                # Add all children of the current node to the queue for the next level
20                if current_node.children:
21                    queue.extend(current_node.children)
22                    
23        return depth