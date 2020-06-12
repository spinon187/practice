class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        paths = [[0]*len(obstacleGrid[0] )for rows in obstacleGrid]
        paths[0][0] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[row])):
                if obstacleGrid[row][col] != 1:
                    if row == 0 and col > 0:
                        paths[row][col] = paths[row][col-1]
                    elif col == 0 and row > 0:
                        paths[row][col] = paths[row-1][col]
                    elif row > 0 and col > 0:
                        paths[row][col] = paths[row-1][col] + paths[row][col-1]
        return paths[-1][-1]