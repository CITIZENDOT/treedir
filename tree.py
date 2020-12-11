import os
import re
from argparse import ArgumentParser

parser = ArgumentParser(
    description="list contents of directories in a tree-like format."
)

# Listing Options
parser.add_argument(
    "-a", help="All files are listed.", action="store_true", default=False
)
parser.add_argument(
    "-d", help="List directories only.", action="store_true", default=False
)
parser.add_argument(
    "-l",
    help="Follow symbolic links like directories.",
    action="store_true",
    default=False,
)
parser.add_argument(
    "-f",
    help="Print the full path prefix for each file.",
    action="store_true",
    default=False,
)
parser.add_argument(
    "-x", help="Stay on current filesystem only.", action="store_true", default=False
)
parser.add_argument("-L", help="Descend only level directories deep.", metavar="level")
parser.add_argument(
    "-R",
    help="Rerun tree when max dir level reached.",
    action="store_true",
    default=False,
)
parser.add_argument(
    "-P", help="List only those files that match the pattern given.", metavar="pattern"
)
parser.add_argument(
    "-I", help="Do not list files that match the given pattern.", metavar="pattern"
)
parser.add_argument(
    "--ignore-case",
    help="Ignore case when pattern matching.",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--matchdirs",
    help="Include directory names in -P pattern matching.",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--noreport",
    help="Turn off file/directory count at end of tree listing.",
    action="store_true",
    default=False,
)
parser.add_argument(
    "--charset",
    help="Use charset X for terminal/HTML and indentation line output.",
    metavar="X",
)
parser.add_argument(
    "--filelimit",
    help="Do not descend dirs with more than # files in them.",
    metavar="#",
)
parser.add_argument(
    "--timefmt",
    help="Print and format time according to the format <f>.",
    metavar="<f>",
)
parser.add_argument("-o", help="Output to file instead of stdout.", metavar="filename")


args = parser.parse_args()
print(args)
