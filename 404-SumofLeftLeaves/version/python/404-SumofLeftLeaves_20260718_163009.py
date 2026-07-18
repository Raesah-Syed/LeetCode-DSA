# Last updated: 7/18/2026, 4:30:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
9        if not root:
10            return []
11
12        q=[root]
13        r=[]
14
15        while q:
16
17            l=len(q)
18            s=0
19
20            for _ in range(l):
21                x=q.pop(0)
22                s+=x.val
23
24                if x.left:
25                    q.append(x.left)
26                    
27                if x.right:
28                    q.append(x.right)
29
30            r.append(s/l)
31                    
32        return r
33            
34               
35         
36            