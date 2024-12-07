#!/usr/bin/env python3
def island_perimeter(grid):
    rows = len(grid)
    culs = len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(culs):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4
                
                # Subtract sides for each adjacent land cell
                if i > 0 and grid[i-1][j] == 1:  # Cell above
                    perimeter -= 1
                if i < rows - 1 and grid[i+1][j] == 1:  # Cell below
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:  # Cell to the left
                    perimeter -= 1
                if j < culs - 1 and grid[i][j+1] == 1:  # Cell to the right
                    perimeter -= 1

    return perimeter

