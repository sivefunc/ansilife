from .end_of_line import end_of_line
from .get_consecutive_number import get_consecutive_number

cell = {
    'b': 0, # Dead cell
    'o': 1  # alive cell
        }

def rle_to_matrix(path):
    """
    return a NxM matrix containing the representation of RLE
    """

    # https://conwaylife.com/wiki/Run_Length_Encoded
    matrix, row = [], []

    with open(path) as rle:
        rle = [l for l in rle.readlines() if '#' not in l] # Removing headers
    
    columns = get_consecutive_number(rle[0], rle[0].index(',')) # Header line
    for line in rle[1:]: # 
        for idx, ch in enumerate(line):
            if ch == '$':
                row = end_of_line(line, idx,  columns, row, matrix)

            elif ch in cell:
                row.extend([cell[ch]] * get_consecutive_number(line, idx))

            elif ch == '!': # Anything after the ! is ignored
                if len(row) < columns:
                    row.extend([0] * (columns - len(row))) # Fill spaces
                matrix.append(row)
                return matrix
