import math

def minimax(depth, node_index, is_max, scores, target_depth):
    # Terminal node reached
    if depth == target_depth:
        return scores[node_index]

    if is_max:
        return max(minimax(depth + 1, node_index * 2, False, scores, target_depth),
                   minimax(depth + 1, node_index * 2 + 1, False, scores, target_depth))
    else:
        return min(minimax(depth + 1, node_index * 2, True, scores, target_depth),
                   minimax(depth + 1, node_index * 2 + 1, True, scores, target_depth))

# 8 Leaf node values representing end-game states
leaf_scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_depth = int(math.log2(len(leaf_scores)))

optimal_value = minimax(0, 0, True, leaf_scores, tree_depth)
print(f"The optimal value calculated via Minimax is: {optimal_value}")
