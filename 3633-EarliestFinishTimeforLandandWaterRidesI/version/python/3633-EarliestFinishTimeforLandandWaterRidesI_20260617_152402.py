# Last updated: 6/17/2026, 3:24:02 PM
# Optimized solution
1class Solution:
2    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
3        def count_soldiers(row: List[int]) -> int:
4            # Binary search to find the first occurrence of 0
5            low, high = 0, len(row)
6            while low < high:
7                mid = (low + high) // 2
8                if row[mid] == 1:
9                    low = mid + 1  # Soldier found, look right
10                else:
11                    high = mid     # Civilian found, look left
12            return low # This will equal the total count of 1s
13
14        # Pair each row index with its soldier count
15        row_strengths = []
16        for i in range(len(mat)):
17            row_strengths.append((count_soldiers(mat[i]), i))
18        
19        # Sort primarily by soldier count. 
20        # Python's Timsort is stable, maintaining index order for ties!
21        row_strengths.sort(key=lambda x: x[0])
22        
23        # Extract the original row indices of the k weakest rows
24        return [row[1] for row in row_strengths[:k]]