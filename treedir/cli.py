#!/usr/bin/env python3
import click
from .treedir import main


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options


options = [
    click.option(
        "-a", "all_files", help="All files are listed.", is_flag=True, default=False
    ),
    click.option(
        "-d", "only_dirs", help="List directory only.", is_flag=True, default=False
    ),
    click.option(
        "-l",
        "sym_links",
        help="Follow symbolic links like subdirectories.",
        is_flag=True,
        default=False,
    ),
    click.argument("directory_list", type=click.Path(exists=True), nargs=-1),
]


@click.command()
@add_options(options)
def cli(directory_list, sym_links, only_dirs, all_files):
    total_dirs = 0
    total_files = 0
    directory_list = list(directory_list)
    if not directory_list:
        directory_list = ["."]

    for directory in directory_list:
        _dirs, _files = main(start_path=directory)
        total_dirs += _dirs
        total_files += _files

    print("\n{0} directories, {1} files".format(total_dirs, total_files))


if __name__ == "__main__":
    cli()
