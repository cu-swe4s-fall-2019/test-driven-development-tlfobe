import matplotlib.pyplot as plt
import numpy as np
import math_lib
import matplotlib
matplotlib.use('Agg')


def boxplot(L, out_file_name="boxplot.png"):
    if L is None:
        raise TypeError("boxplot : Please supply a list and")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("boxplot : Incorrect input type, "
                        + "please supply a list!")

    if len(L) == 0:
        raise IndexError("boxplot : Unpopulated list!")

    list_types = [not isinstance(val, (float, int, complex,
                                       np.float, np.int, np.complex
                                       )
                                 )
                  for val in L]

    if any(list_types):
        raise TypeError("boxplot : List contains invalid type!")

    if type(out_file_name) != str:
        raise TypeError("boxplot : filename is invalid type!")

    else:
        fig = plt.figure(figsize=(3, 3), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.title.set_text("Mean : "+str(math_lib.list_mean(L)) +
                          " St-Dev : "+str(math_lib.list_stdev(L)))
        ax.set_ylabel("Values")

        ax.boxplot(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except PermissionError:
        raise PermissionError(
            "boxplot : Unable to write to "+out_file_name +
            ". Check file permissions!")
    except TypeError:
        raise TypeError(
            "boxplot : Incompatible file extension on "+out_file_name)


def histogram(L, out_file_name="histogram.png"):
    if L is None:
        raise TypeError("histogram : Please supply a list and")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("histogram : Incorrect input type, "
                        + "please supply a list!")

    if len(L) == 0:
        raise IndexError("histogram : Unpopulated list!")

    list_types = [not isinstance(val, (float, int, complex,
                                       np.float, np.int, np.complex))
                  for val in L]

    if any(list_types):
        raise TypeError("histogram : List contains invalid type!")

    if type(out_file_name) != str:
        raise TypeError("histogram : filename is invalid type!")
    else:
        fig = plt.figure(figsize=(3, 3), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.title.set_text("Mean : "+str(math_lib.list_mean(L)) +
                          " St-Dev : "+str(math_lib.list_stdev(L)))
        ax.set_ylabel("Values")
        ax.set_xlabel("Frequency")

        ax.hist(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except PermissionError:
        raise PermissionError(
            "histogram : Unable to write to "+out_file_name +
            ". Check file permissions!")
    except TypeError:
        raise TypeError(
            "histogram : Incompatible file extension on "+out_file_name)


def combo(L, out_file_name="hist_boxplot_combo.png"):
    if L is None:
        raise TypeError("combo : Please supply a list and")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("combo : Incorrect input type, "
                        + "please supply a list!")

    if len(L) == 0:
        raise IndexError("combo : Unpopulated list!")

    list_types = [not isinstance(val, (float, int, complex,
                                       np.float, np.int, np.complex))
                  for val in L]

    if any(list_types):
        raise TypeError("combo : List contains invalid type!")

    if type(out_file_name) != str:
        raise TypeError("combo : filename is invalid type!")
    else:
        fig = plt.figure(figsize=(3, 3), dpi=300)
        plt.suptitle("Mean : "+str(math_lib.list_mean(L)) +
                     " St-Dev : "+str(math_lib.list_stdev(L)))

        # Histogram
        ax1 = fig.add_subplot(2, 1, 1)
        ax1.set_ylabel("Values")
        ax1.set_xlabel("Frequency")
        ax1.hist(L)

        # BoxPlot
        ax2 = fig.add_subplot(2, 1, 2)
        ax2.set_ylabel("Values")
        ax2.boxplot(L)
    try:
        plt.savefig(out_file_name, bbox_inches='tight')
    except PermissionError:
        raise PermissionError(
            "combo : Unable to write to "+out_file_name +
            ". Check file permissions!")
    except TypeError:
        raise TypeError(
            "combo : Incompatible file extension on "+out_file_name)
