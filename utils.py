def is_double_page_spread(width: int, mean: float, std: float) -> bool:
    """
    Given the width of an image as well as some statistical information
    representing the distribution of widths in an imageset,
    determine if the image is a double page spread or not
    Arguments:
    width: int - The width of the image in pixels
    mean: float - The mean width of the imageset
    std: The standard deviation of the width of the imageset
    Returns (bool): True if the image is a double page spread, False otherwise
    """
    if width > mean:
        return True
    else:
        return False
