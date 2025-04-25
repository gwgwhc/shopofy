import numpy as np


def load_rqmap(filename, skiprows=1, delimiter=","):
    """
    Imports the rqmap from a file.

    Args:
        filename (str): The two column file with the rqmap's x and z.
        skiprows (int): Rows to skip.
        delimiter (str): File delimiter.

    Returns:
        arr: Two column array of position x and impedance z.
    """
    rqmap = np.transpose(np.loadtxt(filename, skiprows=skiprows, delimiter=delimiter))
    return rqmap


def generate_rqmap(x_range: float = 400, dispersion: float = 66.9, dp: bool = False):
    # TODO: Make this read parameters for the cavity from a class file.
    """ "
    Generates the rqmap for R3's elliptical cavity.

    Args:
        x_range (float): X position range.
        dispersion (float): Dispersion in mm/% if using dp=True
        dp (bool): If true, x_range is in units of dp/p (%)

    Returns:
    """
    if dp:
        acceptance = x_range / dispersion
    else:
        acceptance = x_range

    rqmap_x = np.linspace(-acceptance / 2, acceptance / 2, int(1e6))
    rqmap_z = np.linspace(128, 0, int(1e6))
    final_map = np.row_stack((rqmap_x, rqmap_z))

    return final_map


# TODO: make function to generate and output rqmap


def get_position(rqmap, power: str):
    """
    Gets position from a given power.

    Args:
        array (array): target rqmap to search, must be two column x, z.
        value (float): power value to search for inside the array.

    Returns:
        int: index of the queried value inside the array.
    """
    index = np.argmin(np.abs(rqmap[1] - power))
    return rqmap[0][index]
