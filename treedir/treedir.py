import os
from colorama import Fore, Style


def main(total_dirs=0, total_files=0, prefix="", current_dir="."):
    for root, dir_names, files in os.walk(current_dir):
        # if os.path.normpath(root) == os.path.normpath(current_dir):
        #     print(
        #         Fore.BLUE,
        #         Style.BRIGHT,
        #         current_dir,
        #         Style.RESET_ALL,
        #         sep="",
        #     )
        # else:
        #     print(
        #         os.path.normpath(root),
        #         os.path.normpath(current_dir)
        #     )
        for file in files:
            print(prefix + "├──", file)
        total_files += len(files)
        total_dirs += len(dir_names)
        for dir_name in dir_names:
            print(
                prefix + "├── ",
                Fore.BLUE,
                Style.BRIGHT,
                dir_name,
                Style.RESET_ALL,
                sep="",
            )
            main(prefix=prefix + "│   ", current_dir=os.path.join(root, dir_name))
    return (total_dirs, total_files)


if __name__ == "__main__":
    main()
