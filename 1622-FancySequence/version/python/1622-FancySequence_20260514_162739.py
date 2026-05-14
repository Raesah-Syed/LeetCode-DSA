# Last updated: 5/14/2026, 4:27:39 PM
# Write the changes happening in input to get to output. Break the operations to a simpler point and then continue. For example here the matrix is first transposed and then reversed at column
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        
7        for i in range(len(matrix)):
8            for j in range(i+1,len(matrix)):
9                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
10
11      
12        for k in range(len(matrix)):
13           matrix[k]=matrix[k][::-1]
14        return (matrix)