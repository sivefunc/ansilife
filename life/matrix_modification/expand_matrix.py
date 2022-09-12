from copy import deepcopy

def expand_matrix(matrix):
    matrix = deepcopy(matrix)
    if matrix == [[]]:
        return matrix

    try:
        up_border = matrix[0]
        down_border = matrix[-1]
        right_border = [matrix[y][-1] for y in range(len(matrix))]
        left_border = [matrix[y][0] for y in range(len(matrix))]
    
    except IndexError:
        return matrix

    if any(up_border): matrix.insert(0, [0] * len(up_border))
    if any(down_border): matrix.append([0] * len(down_border))
    if any(left_border): [row.insert(0, 0) for row in matrix]
    if any(right_border): [row.append(0) for row in matrix]

    return matrix
