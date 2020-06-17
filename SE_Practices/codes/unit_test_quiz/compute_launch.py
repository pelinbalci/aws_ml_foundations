def days_until_launch(current_day, launch_day):
    """
    :param current_day: int
    :param launch_day: int
    :return: the days left before launch.
    """

    return max(launch_day - current_day, 0)
