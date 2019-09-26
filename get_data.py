
def read_stdin_col(col_num):
    if col_num is None:
        raise TypeError("read_stdin_col : Please provide a column number!")
    if not isinstance(col_num, int):
        raise TypeError("read_stdin_col : Incorrect input type!")
    return None
