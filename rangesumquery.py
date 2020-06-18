class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            self.matrix = []
            return
        self.matrix = [[0] * (len(matrix[0])+1) for _ in range(len(matrix) + 1)]
        for row, subarray in enumerate(matrix):
            for col, value in enumerate(subarray):
                self.matrix[row+1][col+1] = self.matrix[row+1][col] + value
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                self.matrix[row+1][col+1] += self.matrix[row][col+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.matrix:
            return 0
        return self.matrix[row2+1][col2+1] + self.matrix[row1][col1] \
            -  self.matrix[row1][col2+1] - self.matrix[row2+1][col1]