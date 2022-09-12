from .cell_neighbors import cell_neighbors

def live_neighbors(Y1, X1, matrix):
    """
    Return the indexs of live neighbors of the current cell in the
    position Y, X in a given  matrix
    """

    live_neighbors = []
    
    for Y2, X2 in cell_neighbors(Y1, X1):
        if Y2 in range(len(matrix)) and X2 in range(len(matrix[Y2])):
            if matrix[Y2][X2]: # Live neighbor = 1, Dead neighbor = 0
                live_neighbors.append((Y2, X2))
    return live_neighbors
