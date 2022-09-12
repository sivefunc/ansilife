from copy import deepcopy

def reduce_matrix(matrix):
    """
    return a matrix with a reduced border
    """

    matrix = deepcopy(matrix)
    
    if matrix == [[]]:
        return matrix

    if len(matrix) > 1:
        up_borders = matrix[0] + matrix[1]
        down_borders = matrix[-1] + matrix[-2]

    else:
        up_borders = down_borders = [True] # maximum reduction in rows reached
    
    try:
        r_borders = [matrix[y][i] for y in range(len(matrix)) for i in [-1,-2]]
        l_borders = [matrix[y][i] for y in range(len(matrix)) for i in [0, 1]]
    
    except IndexError: # Maximum reduction in columns reached
        r_borders = l_borders = [True]

    if not any(up_borders): matrix.pop(0)
    if not any(down_borders): matrix.pop()
    if not any(l_borders): [row.pop(0) for row in matrix]
    if not any(r_borders): [row.pop() for row in matrix]

    return matrix
