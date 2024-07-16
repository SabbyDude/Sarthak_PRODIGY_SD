def maxTreasure(m, n, grid):
    dp = [[0] * n for _ in range(m)]
    path = [[None] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    
    # Initialize the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
        path[0][j] = (0, j - 1)
    
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
        path[i][0] = (i - 1, 0)
    
    for i in range(1, m):
        for j in range(1, n):
            if dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
                path[i][j] = (i - 1, j)
            else:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
                path[i][j] = (i, j - 1)
    
    max_treasure = dp[m - 1][n - 1]
    current = (m - 1, n - 1)
    path_taken = []
    while current:
        path_taken.append(current)
        current = path[current[0]][current[1]]
    path_taken.reverse()

    return max_treasure, path_taken

def main():
    m, n = map(int, input("Enter dimensions of the matrix (m n): ").split())
    print(f"Enter the {m}x{n} matrix row by row:")
    grid = []
    for i in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    max_treasure, path_taken = maxTreasure(m, n, grid)
    print("Maximum amount of treasure that can be collected:", max_treasure)
    print("Path taken to collect the treasure:", path_taken)
    
    # Verify the sum of the path
    path_sum = sum(grid[i][j] for i, j in path_taken)
    print("Sum of values along the path:", path_sum)

main()
