from PIL import Image # To create a gif
from sys import stdout # print faster alternative
from time import sleep # delay between each generation
from os import get_terminal_size # to fill screen according to terminal

from soup import soup # generate random pattern
from parser import parser # get arguments of the terminal

# If pattern is given or wants to save generation
from RLE.rle_to_matrix import rle_to_matrix # RLE decoder
from RLE.matrix_to_rle import matrix_to_rle # RLE encoder
from matrix_to_img import matrix_to_image # generate image to put inside gif

from matrix_graphics import matrix_with_graphics # gen terminal graphics
from generation.make_generation import make_generation # make gen :O

# Make modifications according to the arguments given
from matrix_modification.fill_matrix import fill_matrix
from matrix_modification.expand_matrix import expand_matrix
from matrix_modification.reduce_matrix import reduce_matrix


ESC = chr(27)
CSI = ESC + '['

write = stdout.write # Faster tha print
args = parser()

def main():
    if args.pattern:
        matrix = rle_to_matrix(args.pattern) # Decode rle
        if args.fill:
            # fills the surrounding area of the matrix with the size of term
            X, Y = get_terminal_size()[0], get_terminal_size()[1] - 1
            matrix = fill_matrix(Y, X, matrix)

        elif args.rows:
            # fills the surrounding area of the matrix vertically
            # and maybe horizontally?, if it's given too
            X, Y = (args.columns,args.rows) if args.columns else (-1,args.rows)
            matrix = fill_matrix(Y, X, matrix)

        elif args.columns:
            # fills the surrounding area of the matrix horizontally
            matrix = fill_matrix(-1, args.columns, matrix)

    else: # Pattern was not given, generate a random pattern
        matrix = soup(args.rows, args.columns, fill=args.fill)
    
    if args.gif:
        images = [matrix_to_image(matrix, dark=args.dark_mode)]

    else:
        write(f'{CSI}2J{CSI}H' + matrix_with_graphics(matrix,
                                        dark=args.dark_mode))
    
    for generation in range(args.gen):
        if args.expand_matrix: # Allow game to expand infinitely
            matrix = expand_matrix(matrix)

        if args.reduce_matrix: # Save memory to remove space not used
            matrix = reduce_matrix(matrix)

        matrix = make_generation(matrix)
        terminal_matrix = matrix_with_graphics(matrix, dark=args.dark_mode)
        sleep(args.delay)
        if args.gif:
            images.append(matrix_to_image(matrix, dark=args.dark_mode))
        
        else:
            write(f'{CSI}2J{CSI}H' + terminal_matrix)

    if args.save:
        matrix_to_rle(matrix, args.save)

    if args.gif: # 10 fps
        images.pop(0).save(args.gif, save_all=True, append_images=images)

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt as error:
        pass # exit
