# Last updated: 6/18/2026, 10:31:16 PM
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldiers(row: List[int]) -> int:
            # Binary search to find the first occurrence of 0
            low, high = 0, len(row)
            while low < high:
                mid = (low + high) // 2
                if row[mid] == 1:
                    low = mid + 1  # Soldier found, look right
                else:
                    high = mid     # Civilian found, look left
            return low # This will equal the total count of 1s

        # Pair each row index with its soldier count
        row_strengths = []
        for i in range(len(mat)):
            row_strengths.append((count_soldiers(mat[i]), i))
        
        # Sort primarily by soldier count. 
        # Python's Timsort is stable, maintaining index order for ties!
        row_strengths.sort(key=lambda x: x[0])
        
        # Extract the original row indices of the k weakest rows
        return [row[1] for row in row_strengths[:k]]