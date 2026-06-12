from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    bfs_order = []
    
    while queue:
        vertex = queue.popleft()
        bfs_order.append(vertex)
        
        # Check all neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return bfs_order

# Example Graph Representation (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Traversal starting from 'A':")
print(bfs(graph, 'A'))
