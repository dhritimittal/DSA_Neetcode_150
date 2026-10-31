class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        path = [[0] * n for _ in range(m)]

        path[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and path[i - 1][0] == 1:
                path[i][0] = 1

        for i in range(1, n):
            if obstacleGrid[0][i] == 0 and path[0][i - 1] == 1:
                path[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[m - 1][n - 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna