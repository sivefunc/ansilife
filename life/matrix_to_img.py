from PIL import Image

color = {
        0: {False: 255, True: 0},
        1: {False: 0, True: 255}}

def matrix_to_image(matrix, dark=False):
    """
    return an image representing the matrix
    """

    # flat list of values containing either 255 or 0
    pixels = [color[cell][dark] for cells in matrix for cell in cells]

    #  # 1bit color  - (width and height)
    image = Image.new('L', [len(matrix[0]), len(matrix)]) 
    image.putdata(pixels)

    return image
