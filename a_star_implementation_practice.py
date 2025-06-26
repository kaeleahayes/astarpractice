# a_star_implementation_practice
# Based on Wikipedia's A* search algorithm code and Geeks4Geeks A* in Python guide
# Kaelea Hayes
# 2025-06-26

import math
import heapq

# Define grid cell class
class Cell:
    def __init__(self):
        # Define parent cell indicies and f = g + h costs
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

# Define overall grid size
ROW = 9
COL = 10

# Cell validity checks
def is_valid(row, col):
    return (row>=0) and (row < ROW) and (col >= 0) and (col<COL)

def is_unblocked(grid,row,col):
    return grid[row][col] == 1

def is_destination(row,col,dest):
    return row == dest[0] and col == dest[1]
 
def h(row, col, goal):
    # Define heuristic as Euclidean distance to search goal
    return ((row - goal[0])**2 + (col - goal[1])**2)**0.5

def reconstruct_path(cells, goal_node):
    print('The path is')
    total_path = []
    row = goal_node[0]
    col = goal_node[1]

    while not (cells[row][col].parent_i == row and cells[row][col].parent_j == col):
        total_path.append((row,col))
        temp_row = cells[row][col].parent_i
        temp_col = cells[row][col].parent_j
        row = temp_row
        col = temp_col
    
    total_path.append((row,col))
    total_path.reverse()

    # Print path
    for i in total_path:
        print('->',i,end=" ")
    print()

def a_star(grid,start_node, goal_node):
    # Initialize set of discovered nodes. 
    open_set = []
    # Closed node list
    closed_set = [[False for _ in range(COL)] for _ in range(ROW)]

    # Create list of all cells based on grid dimensions
    cells = [[Cell() for _ in range(COL)] for _ in range(ROW)]

    # Start point characteristics
    i = start_node[0]
    j = start_node[1]
    cells[i][j].f = 0
    cells[i][j].g = 0
    cells[i][j].h = 0
    cells[i][j].parent_i = i
    cells[i][j].parent_j = j

    # Create heap to allow easier search methods
    heapq.heappush(open_set, (0.0, i, j))

    # Open list search
    while not len(open_set) == 0:
        # Select lowest f value from open list ('current node')
        current_node = heapq.heappop(open_set)
        # Check if current node is goal node

        # Move current node to closed list
        i = current_node[1]
        j = current_node[2]
        closed_set[i][j] = True

        # Neighbor search
        directions = [(0,1), (0,-1), (1,0), (-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # Validity check
            if is_valid(new_i,new_j) and is_unblocked(grid, new_i, new_j) and not closed_set[new_i][new_j]:
                if is_destination(new_i,new_j,goal_node):
                    # Set parent of destination cell
                    cells[new_i][new_j].parent_i = i
                    cells[new_i][new_j].parent_j = j
                    print('The goal has been found')
                    # Trace path back from start to finish
                    reconstruct_path(cells,goal_node)
                    return
                else:
                    g_new = cells[i][j].g + 1.0
                    h_new = h(new_i,new_j,goal_node)
                    f_new = g_new + h_new
                    # If the cell is not in the open list or the new value of f is smaller
                    if cells[new_i][new_j].f == float('inf') or cells[new_i][new_j].f > f_new:
                        heapq.heappush(open_set, (f_new, new_i, new_j))
                        # Update cell data
                        cells[new_i][new_j].f = f_new
                        cells[new_i][new_j].g = g_new
                        cells[new_i][new_j].h = h_new
                        cells[new_i][new_j].parent_i = i
                        cells[new_i][new_j].parent_j = j

            
    # Open list empty failure case
    print('The search algorithm failed.')

        
def main():
    # Define grid, start, and goal
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    start = [8, 9]
    goal = [0, 0]

    # Run A* Algorithm
    a_star(grid,start,goal)

if __name__ == "__main__":
    main()