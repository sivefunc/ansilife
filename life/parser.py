import argparse

def parser():
    parser = argparse.ArgumentParser(
            prog="AnsiLife",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            usage='%(prog)s [options]',
            description="Simple unix terminal game of life viewer")

    parser.add_argument(
            '-v','--version',
            action='version',
            version="""
%(prog)s v1.0.0
Copyright (C) 2022 Sivefunc
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human""")

    parser.add_argument(
            '-p', '--pattern',
            type=str,
            help='path of the pattern file encoded in erl format',
            metavar="")
    
    parser.add_argument(
            '-g', '--gen',
            default=82,
            help='number of generations to occur in pattern',
            metavar="",
            type=lambda n: int(n) if float(n) >= 0 and n.isdigit() else exit(
                'usage: ' + parser.prog + ' [options]\n' +
                parser.prog + f": error: argument -g/--gen: number isn't "\
                                f"positive integer: {n}")) 
   
    parser.add_argument(
            '-d', '--delay',
            help='delay between each generation',
            default=0.1,
            metavar="",
            type=lambda n: float(n) if float(n) >= 0 else exit(
                'usage: ' + parser.prog + ' [options]\n' +
                parser.prog + f": error: argument -d/--delay: number isn't "\
                                f"positive: {n}"))

    parser.add_argument(
            '-r', '--rows',
            type=int,
            help='number of rows that pattern should have',
            metavar="")

    parser.add_argument(
            '-c', '--columns',
            type=int,
            help='number of columns that pattern should have',
            metavar="")

    parser.add_argument(
            '-f', '--fill',
            action="store_true",
            help='number of rows and columns the same as terminal screen')
    
    parser.add_argument(
            '-rm', '--reduce-matrix',
            action="store_true",
            help="reduce matrix border if it's not being used by pattern")
    
    parser.add_argument(
            '-em', '--expand-matrix',
            action="store_true",
            help="expand matrix border if it's being used by pattern")
     
    parser.add_argument(
            '-sv', '--save',
            help="save the last generation of pattern to a given path encoded in rle",
            metavar="")
    
    parser.add_argument(
            '--gif',
            help="save all the generations into a gif (10 fps)",
            metavar="")

    parser.add_argument(
            '-dk', '--dark-mode',
            action="store_true",
            help="graphics of pattern will be black background and white foreground")

    args = parser.parse_args()
    return args
