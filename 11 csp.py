def is_safe(node, color, assignment, graph):
    for neighbor in graph.get(node, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def recursive_csp(assignment, variables, colors, graph):
    if len(assignment) == len(variables):
        return assignment

    # Select unassigned variable
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    for color in colors:
        if is_safe(var, color, assignment, graph):
            assignment[var] = color
            result = recursive_csp(assignment, variables, colors, graph)
            if result:
                return result
            del assignment[var] # Backtrack
            
    return None

# Map variables and their adjacencies
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
colors = ['Red', 'Green', 'Blue']

solution = recursive_csp({}, variables, colors, graph)
print("CSP Map Coloring Assignment:")
print(solution)
