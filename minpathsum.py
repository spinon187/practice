class Solution:
    def minPathSum(self, grid):
        paths = [[0]*len(grid[0])]*len(grid)
        for row in range(len(paths)):
            for col in range(len(paths[row])):
                if row == 0:
                    if col == 0:
                        paths[row][col] = grid[row][col]
                    else:
                        paths[row][col] = grid[row][col] + paths[row][col-1]
                elif col == 0:
                    paths[row][col] = grid[row][col] + paths[row-1][col]
                else:
                    val = grid[row][col]
                    paths[row][col] = min(paths[row-1][col]+val, paths[row][col-1]+val)
        print(paths)
        return paths[-1][-1]