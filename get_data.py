import sys


def read_stdin_col(col_num):
    if col_num is None:
        raise TypeError("read_stdin_col : Please provide a column number!")
    if not isinstance(col_num, int):
        raise TypeError("read_stdin_col : Incorrect input type!")

    stdin = sys.stdin.readlines()
    if len(stdin[0].rstrip().split(' ')) < col_num:
        print(stdin[0].rstrip().split(' '))
        raise IndexError("read_stdin_col : col_num is out of range!")

    column = []
    for line in stdin:
        value = line.rstrip().split(' ')[col_num]
        column.append(int(value))
    return column
