from os import get_terminal_size as gtsize
from random import randint, randrange, choices

def soup(rows, columns, fill=False): 
    """
    return a soup according to the given rows and columns
    """
    
    # https://conwaylife.com/wiki/Soup

    if fill: # Width and  height will occupy the entire terminal
        X, Y = gtsize()[0], gtsize()[1] - 1

    elif rows:
        if columns: # Choose the given limits
            X, Y = columns, rows

        else: # Only row was given, choose a random width
           X, Y = randint(int(gtsize()[0] / 3), gtsize()[0]), rows

    elif columns: # Only columns was given, choose a ramdom height
        X, Y = columns, randrange(int(gtsize()[1] / 3), gtsize()[1])

    
    else: # If no limit was given choose random width and height
        X = randint(int(gtsize()[0] / 3), gtsize()[0])
        Y = randrange(int(gtsize()[1] / 3), gtsize()[1])

    matrix = [[0] * X for row in range(Y)] # dead matrix

    cells_counter = Y * X # total cells
    
    # how many live cells wil be there
    density = int((cells_counter/choices([2, 3, 4, 5],[50,30,20,10])[0]))

    live_cells = set()
    while len(live_cells) < density:
        # Choose a random cordinate and pick it if it's dead
        row, column = randrange(0, Y), randrange(0, X)
        live_cells.add((row, column))

    for Y, X in live_cells: matrix[Y][X] = 1 # Make the canges

    return matrix
