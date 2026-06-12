from itertools import permutations

def calculate_path_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]] # Return back to starting node
    return cost

def travelling_salesman_problem(graph, start_node):
    # Get all cities/nodes except the starting city
    nodes = list(graph.keys())
    nodes.remove(start_node)
    
    min_cost = float('inf')
    best_path = []
    
    # Generate all permutations of the remaining cities
    for perm in permutations(nodes):
        current_path = [start_node] + list(perm)
        current_cost = calculate_path_cost(graph, current_path)
        
        # Track the route with the lowest cost
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
            
    return best_path + [start_node], min_cost

# Example Graph Matrix representation (Adjacency Matrix as a nested dictionary)
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

start_city = 'A'
path, cost = travelling_salesman_problem(graph, start_city)

print(f"Starting City: {start_city}")
print(f"Optimal TSP Path: {' -> '.join(path)}")
print(f"Minimum Distance/Cost: {cost}")
