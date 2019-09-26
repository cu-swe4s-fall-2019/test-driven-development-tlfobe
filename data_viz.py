import numpy as np
import math_lib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

    if type(out_file_name) != str:
        raise TypeError("boxplot : filename is invalid type!")
    
    else:
        fig= plt.figure(figsize=(10,10), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.title.set_text("Mean : "+str(math_lib.list_mean(L))+ \
                        " St-Dev : "+str(math_lib.list_stdev(L)))
        ax.set_ylabel("Values")
        
        ax.boxplot(L)
        plt.savefig(out_file_name, bbox_inches='tight')
        return 0






def histogram(L, out_file_name = "histogram.png"):
    if L is None:
        raise TypeError("histogram : Please supply a list and")

    if not isinstance(L, (list, np.ndarray)):
        raise TypeError("histogram : Incorrect input type, "
                        + "please supply a list!")

    if len(L) == 0:
        raise IndexError("histogram : Unpopulated list!")

    list_types = [not isinstance(val, (float, int, complex, np.float, np.int, np.complex))
                  for val in L]

    if any(list_types):
        raise TypeError("histogram : List contains invalid type!")

    if type(out_file_name) != str:
        raise TypeError("histogram : filename is invalid type!")
    else:
        fig= plt.figure(figsize=(10,10), dpi=300)
        ax = fig.add_subplot(1, 1, 1)
        ax.title.set_text("Mean : "+str(math_lib.list_mean(L))+ \
                        " St-Dev : "+str(math_lib.list_stdev(L)))
        ax.set_ylabel("Values")
        ax.set_xlabel("Frequency")
        
        ax.hist(L)
        plt.savefig(out_file_name, bbox_inches='tight')


def combo(L, out_file_name):
    pass
