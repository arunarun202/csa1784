from collections import deque

# State representation: (M_left, C_left, Boat_position)
# Boat_position: 1 for left bank, 0 for right bank
START = (3, 3, 1)
GOAL = (0, 0, 0)

def is_valid(m, c):
    # Check if numbers are negative or exceed total limits
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # Check if cannibals outnumber missionaries on either bank
    if m > 0 and m < c:  # Left bank
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):  # Right bank
        return False
    return True

def get_successors(state):
    m, c, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] # Possible boat configurations
    successors = []

    for dm, dc in moves:
        if boat == 1: # Moving Left to Right
            nm, nc = m - dm, c - dc
            next_state = (nm, nc, 0)
        else: # Moving Right to Left
            nm, nc = m + dm, c + dc
            next_state = (nm, nc, 1)

        if is_valid(nm, nc):
            successors.append(next_state)
            
    return successors

def solve_missionaries_cannibals():
    queue = deque([(START, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue
        visited.add(current)

        current_path = path + [current]

        if current == GOAL:
            return current_path

        for successor in get_successors(current):
            if successor not in visited:
                queue.append((successor, current_path))
    return None

# Run and format output
solution = solve_missionaries_cannibals()
if solution:
    print("Missionaries & Cannibals State Path (M, C, Boat):")
    for step in solution:
        bank = "Left" if step[2] == 1 else "Right"
        print(f"Left Bank: {step[0]}M, {step[1]}C | Boat is on: {bank}")
else:
    print("No solution found.")
