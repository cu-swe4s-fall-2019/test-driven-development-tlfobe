import sys
import numpy as np


def list_mean(L):
    if L is None:
        raise TypeError("list_mean : Please supply a list!")

    if not isinstance(L, list):
        raise TypeError("list_mean : Incorrect input type, \
                         please supply a list!")

    if len(L) == 0:
        raise IndexError("list_mean : Unpopulated list!")

    list_types = [not isinstance(L, (float, int, complex, np.float, np.int, np.complex))]

    if any(list_types):
        raise TypeError("list_mean : List contains invalid type!")
    



def list_stdev(L):
    return None
