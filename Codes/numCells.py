def numCells(grid):
    # Get the dimensions of the grid
    n = len(grid)
    m = len(grid[0])
    
    # Helper function to check if a cell is dominant
    def is_dominant(x, y):
        # List of all possible directions for neighbors
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[x][y] <= grid[nx][ny]:
                    return False
        return True
    
    # Count dominant cells
    dominant_count = 0
    for i in range(n):
        for j in range(m):
            if is_dominant(i, j):
                dominant_count += 1
    
    return dominant_count
