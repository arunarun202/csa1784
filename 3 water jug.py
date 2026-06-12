from collections import deque

def solve_water_jug(jug1_cap, jug2_cap, target):
    # Queue stores (amt_in_jug1, amt_in_jug2, path_taken)
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        j1, j2, path = queue.popleft()

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        current_path = path + [(j1, j2)]

        if j1 == target or j2 == target:
            return current_path

        # Rules / Transitions
        moves = [
            (jug1_cap, j2),  # Fill Jug 1
            (j1, jug2_cap),  # Fill Jug 2
            (0, j2),         # Empty Jug 1
            (j1, 0),         # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2)),
            # Pour Jug 2 -> Jug 1
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1))
        ]

        for m in moves:
            if m not in visited:
                queue.append((m[0], m[1], current_path))
                
    return None

# Example: Jug 1 capacity = 4, Jug 2 capacity = 3, Target = 2
steps = solve_water_jug(4, 3, 2)
if steps:
    print("Steps to solve Water Jug problem:")
    for step in steps:
        print(f"Jug1: {step[0]}L, Jug2: {step[1]}L")
else:
    print("No solution possible.")
