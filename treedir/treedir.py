import os
import ntpath
from colorama import Fore, Style

START_SUFFIX = "├── "
END_SUFFIX = "└── "
LINE = "│"


def clean_name(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def main(total_dirs=0, total_files=0, start_path="."):
    for root, dirs, files in os.walk(start_path):
        relativePath = os.path.relpath(root, start_path)
        dirLevel = relativePath.count(os.sep)
        fileLevel = dirLevel + 1
        isStartPath = os.path.abspath(root) == os.path.abspath(start_path)
        total_dirs += 1
        total_files += len(files)

        if isStartPath:
            dirIndent = ""
            fileIndent = START_SUFFIX
        else:
            dirIndent = (
                (LINE * (dirLevel != 0)) + (dirLevel * "   ") + START_SUFFIX
            )
            fileIndent = LINE + (fileLevel * "   ") + START_SUFFIX

        print(
            "{}{}".format(
                dirIndent,
                Fore.BLUE
                + Style.BRIGHT
                + clean_name(root)
                + " "
                + str(dirLevel)
                + Style.RESET_ALL,
            )
        )

        for f in files[:-1]:
            print(
                "{}{}".format(
                    fileIndent,
                    clean_name(f) + Style.RESET_ALL,
                )
            )
        if files:
            if not dirs:
                fileIndent = fileIndent.replace(START_SUFFIX, END_SUFFIX)
            print(
                "{}{}".format(
                    fileIndent,
                    clean_name(files[-1]) + Style.RESET_ALL,
                )
            )

    return (total_dirs - 1, total_files)


if __name__ == "__main__":
    main()
