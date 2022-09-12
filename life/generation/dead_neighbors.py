from .cell_neighbors import cell_neighbors

def dead_neighbors(Y1, X1, matrix):
    """
    Return the indexs of dead neighbors of the current cell in the
    position Y, X in a given matrix
    """

    dead_neighbors = []
    
    for Y2, X2 in cell_neighbors(Y1, X1):
        if Y2 in range(len(matrix)) and X2 in range(len(matrix[Y2])):
            if not matrix[Y2][X2]: # Live neighbor = 1, Dead neighbor = 0
                dead_neighbors.append((Y2, X2))
    return dead_neighbors
