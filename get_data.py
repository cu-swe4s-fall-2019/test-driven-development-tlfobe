import sys

def read_stdin_col(col_num):
    if col_num is None:
        raise TypeError("read_stdin_col : Please provide a column number!")
    if not isinstance(col_num, int):
        raise TypeError("read_stdin_col : Incorrect input type!")
    if len(sys.stdin.readlines()[0].rstrip().split(' ')) > col_num:
        raise IndexError("read_stdin_col : col_num is out of range!")
    
        


    return None