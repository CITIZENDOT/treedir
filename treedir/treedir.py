import os
import ntpath
from colorama import Fore, Style

START_SUFFIX = "├── "
FILE_END_SUFFIX = "└──"
LINE = "│"


def clean_name(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def main(total_dirs=0, total_files=0, start_path="."):
    for root, dirs, files in os.walk(start_path):
        level = os.path.relpath(root, start_path).count(os.sep) + 1
        indent = sub_indent = ""
        if level > 0:
            if level == 1:
                indent = START_SUFFIX
            else:
                indent = (LINE + ("    " * (level - 1))) + START_SUFFIX

        sub_indent = (LINE + ("    " * level)) + START_SUFFIX
        print("{}{}".format(indent, Fore.BLUE + Style.BRIGHT + clean_name(root) + Style.RESET_ALL))
        total_dirs += 1
        for f in files:
            print("{}{}".format(sub_indent, clean_name(f)))
            total_files += 1
    return (total_dirs - 1, total_files)


if __name__ == "__main__":
    main()
