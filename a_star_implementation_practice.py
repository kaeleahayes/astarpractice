# a_star_implementation_practice
# Based on Wikipedia's A* search algorithm code
# Kaelea Hayes
# 2025-06-26

def h(n):
    # h is a heuristic function estimating cost to reach goal from current node
    h = []

def reconstruct_path(came_from, current_node):
    total_path = {current_node}
    
    # Return entire path
    return total_path

def a_star(start_node, goal_node, h):
    # Initialize set of discovered nodes. 
    open_set = {start_node}

    # Previous node along cheapest path from start
    came_from = {}

    # Currently known cost of the cheapest path from start to current node
    g = float('inf')
    g[start_node] = 0

    # Guess about cost of path going through current node
    f = float('inf')
    f[start_node] = h(start_node)

    while not (len(open_set) == 0):
        current_node = [] # node in open_set having lowest f
        if current_node == goal_node:
            # Return entire path 
            return reconstruct_path(came_from, current_node)
        
        # Remove current node from open set
        open_set.remove(current_node)
        # Define set of neighbors,find lowest est. cost
        neighborset = []
        for neighbor in neighborset:
            guess_g = g[current_node] = g[current_node] + d(current_node, neighbor)
            if guess_g < g[neighbor]:
                came_from[neighbor] = current_node
                g[neighbor] = guess_g
                f[neighbor] = guess_g + h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)
    
    # If open set is empty but goal not reached, fail cond:
    return 0
        

