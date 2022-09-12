def matrix_with_graphics(matrix, dark=False):
    ESC = chr(27)
    CSI = ESC + '['

    graphics = ""
    
    for cells in matrix:
        for cell in cells:
            if cell:
                graphics += f'{CSI}40m ' if not dark else f'{CSI}47m '
            
            else:
                graphics += f'{CSI}47m ' if not dark else f'{CSI}40m '

        graphics += f'{CSI}0m\n'
    return graphics
