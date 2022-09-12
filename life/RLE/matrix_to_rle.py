CELL = {
        0: 'b',
        1: 'o'
        }

def matrix_to_rle(matrix, path):
    """
    write to a given file containing the matrix encoded in rle format
    """

    # https://conwaylife.com/wiki/Run_Length_Encoded
    write = [f'x = {len(matrix[0])}, y = {len(matrix)}\n']
    last_cell = 0
    line = ""
    tag = ""

    for cells in matrix:
        for cell in cells: 
            if last_cell != cell and tag: # different cell was found
                # append the given run count and tag
                if len(line) + len(tag) + 1 > 70: # Split every 70 ch
                    write.append(line + '\n')
                    line = f'{len(tag)}{tag[0]}' if len(tag) > 1 else tag
                
                else:
                    line += f'{len(tag)}{tag[0]}' if len(tag) > 1 else tag
                
                tag = CELL[cell] # create new tag
            
            else: # increase tag counter by 1 if not different cell
                tag += CELL[cell]
            last_cell = cell # save the cell to check if next is different

        # end of line reached
        if len(line) + len(tag) + 2 > 70:
            write.append(line + '\n')
            line = f'{len(tag)}{tag[0]}$' if len(tag) > 1 else tag + '$'
        
        else:
            line += f'{len(tag)}{tag[0]}$' if len(tag) > 1 else tag + '$'
        tag = "" # clear the tag
    
    line = line[:-1] + '!' # end of file reached
    write.append(line + '\n')
    
    path += 'pattern.rle' if path.endswith('/') else ''
    try:
        with open(path,'w') as file:
            file.writelines(write)

    except NotADirectoryError as error:
        print(error)
