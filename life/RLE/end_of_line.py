from .get_consecutive_number import get_consecutive_number

def end_of_line(line, idx, columns, row, matrix):
    """
    return an empty row indicating that the matrix has appended the
    given row
    """

    number = get_consecutive_number(line, idx)
    if row:
        if len(row) < columns: # Filling row with dead cells
            row.extend([0] * (columns - len(row)))
        matrix.append(row)

        if number > 1: # <run count>
            for i in range(number-1): matrix.append([0] * columns) # Dead cells
    
    else: # <run count>
        for i in range(number): matrix.append([0] * columns) # Dead cells

    return []
