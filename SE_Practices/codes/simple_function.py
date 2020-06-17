def nearest_square(num):
    """
    :param num: integer
    :return: the nearest square that is less than or equal to sum
    """
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2