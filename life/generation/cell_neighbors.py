def cell_neighbors(Y, X):
    """
    Returh the indexs of each neighbor around the  given cell Y, X
    """

    return (
                [Y - 1, X - 1], [Y - 1, X], [Y - 1, X + 1],
                [Y - 0, X - 1],             [Y - 0, X + 1],
                [Y + 1, X - 1], [Y + 1, X], [Y + 1, X + 1]
            )
