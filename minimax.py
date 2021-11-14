# minimax algorithm
def minimax(position, depth, alpha, beta, maximizingPlayer):
    
    if depth == 0 or gameIsOver:
        return score # static evaluation of position

    if maximizingPlayer:
        maxEval = float("-inf")
        for child in position:
            tempEval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
        
    else:
        minEval = float("inf")
        for child in position:
            tempEval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
