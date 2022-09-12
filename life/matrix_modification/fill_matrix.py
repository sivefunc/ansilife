def fill_matrix(Y, X, matrix1):
    """
    fills the surrounding area of the matrix with the given limits
    """

    matrix2 = []

    if (columns := len(matrix1[0])) < X:
        for idx, cells in enumerate(matrix1):
            left = [0] * int((X - columns) / 2 + 0.5) # Add the half to left
            right = [0] * int((X - columns) / 2) # Add other half to left
            matrix2.append(left + cells + right)

    if (rows := len(matrix2)) < Y and len(matrix1) < Y:
        if not rows: # If X limit wasn't given, so new matrix wasn't created
            rows = len(matrix1)

        columns = len(matrix1[0]) if not matrix2 else len(matrix2[0])
        up = [[0] * columns for i in range(int((Y - rows) / 2 + 0.5))]
        down = [[0] * columns for i in range(int((Y - rows) / 2))]
        matrix2 = up + matrix2 + down if matrix2 else up + matrix1 + down
    
    return matrix2 if matrix2 else matrix1
