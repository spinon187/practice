class Solution:
    def countSquares(self, matrix):
        memo = [[0]*len(matrix[0]) for _ in matrix]
        count = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    memo[row][col] = 1 + min(memo[row][col-1], memo[row-1][col-1], memo[row-1][col])
                    count += memo[row][col]
        return count