from copy import deepcopy
from .live_neighbors import live_neighbors
from .dead_neighbors import dead_neighbors

def make_generation(matrix):
    """
    return the tick also known the generation of the given matrix
    """

    born, die = set(), set()
    matrix = deepcopy(matrix)

    for Y1, cells in enumerate(matrix):
        for X1, cell in enumerate(cells):
            if cell:
                if len(live_neighbors(Y1, X1, matrix)) not in {2, 3}:
                    # Any cell with fewer than two or greater than 3
                    # neighbors dies
                    die.add((Y1, X1))
                
                for Y2, X2 in dead_neighbors(Y1, X1, matrix):
                    if len(live_neighbors(Y2, X2, matrix)) == 3:
                        # Any dead cell with exactly three live neighbours
                        # becomes a live cell
                        born.add((Y2, X2))

    for Y, X in born: matrix[Y][X] = 1
    for Y, X in die: matrix[Y][X] = 0

    return matrix
