import argparse
import get_data
import data_viz
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_file",
                        required=True,
                        help="file to write plot to",
                        type=str,
                        )

    parser.add_argument("--plot_type",
                        required=True,
                        help="type of visualization for data",
                        type=str,
                        choices=["histogram", "boxplot", "combo"]
                        )

    parser.add_argument("--col_number",
                        required=False,
                        help="column of data you want to sumarize",
                        default=0,
                        type=int,
                        )

    parser.add_argument("--in_type",
                        required=False,
                        help="how data will be fed to the program",
                        type = str,
                        default="stdin",
                        choices=["stdin", "file"]
                        )

    args = parser.parse_args()

    
    if args.in_type == "stdin":
        try: 
            data = get_data.read_stdin_col(args.col_number)
        except IndexError:
            print("viz.py : Index "+str(args.col_number)+" is not in STDIN!", file=sys.stderr)
            sys.exit(1)
    if args.in_type == "file":
        print("viz.py : This feature is not implemented yet! Sorry!", file=sys.stderr)
        sys.exit(1)
    if args.plot_type == "histogram":
        try:
            data_viz.histogram(data, out_file_name=args.out_file)
        except IndexError:
            print("viz.py : STDIN list is empty!")
        except PermissionError:
            print("viz.py : Output file "+args.out_file+" is not accessible. Check your permissions!", file=sys.stderr)
    if args.plot_type == "boxplot":
        try:
            data_viz.boxplot(data, out_file_name=args.out_file)
        except IndexError:
            print("viz.py : STDIN list is empty!")
        except PermissionError:
            print("viz.py : Output file "+args.out_file+" is not accessible. Check your permissions!", file=sys.stderr)
    if args.plot_type == "combo":
        try:
            data_viz.combo(data, out_file_name=args.out_file)
        except IndexError:
            print("viz.py : STDIN list is empty!")
        except PermissionError:
            print("viz.py : Output file "+args.out_file+" is not accessible. Check your permissions!", file=sys.stderr)    




if __name__ == '__main__':
    main()
