def alpha_beta(depth, node, is_max, values, alpha, beta):
    if depth == 3:
        return values[node]
    
    if is_max:
        best = float('-inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal Alpha-Beta Value:", alpha_beta(0, 0, True, values, float('-inf'), float('inf')))
