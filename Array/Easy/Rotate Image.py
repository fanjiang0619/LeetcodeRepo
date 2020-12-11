class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        matrix_copy = copy.deepcopy(matrix)
        for i in range(size):
            row = matrix_copy[size - i - 1]
            for k, num in enumerate(row):
                matrix[k][i] = num

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        matrix.reverse()
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])