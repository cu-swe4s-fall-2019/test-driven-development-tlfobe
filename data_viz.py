import numpy as np

def boxplot(L, out_file_name = "boxplot.png"):
    if L is None:
        raise TypeError("boxplot : Please supply a list and")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("boxplot : Incorrect input type, "
                        + "please supply a list!")

    if len(L) == 0:
        raise IndexError("boxplot : Unpopulated list!")

    list_types = [not isinstance(val, (float, int, complex, np.float, np.int, np.complex))
                  for val in L]

    if any(list_types):
        raise TypeError("boxplot : List contains invalid type!")

    if type(out_file_name) ! = str:
        raise TypeError("boxplot : filename is invalid type!")





def histogram(L, out_file_name):
    pass


def combo(L, out_file_name):
    pass
