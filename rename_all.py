from os import walk, rename
from argparse import ArgumentParser


parser = ArgumentParser(description="Renames all the letters/words of directories and/or files.")

parser.add_argument("old", type=str, help="Old letter/word")
parser.add_argument("new", type=str, help="New letter/word")
parser.add_argument("-p", "--path", type=str, help="Destination path (default \".\")")

args = parser.parse_args()

if not args.path:
    args.path = '.'

for root, dirs, files in walk(args.path):
    for old_dir in dirs:
        new_dir = old_dir.replace(args.old, args.new)
        rename(f"{root}/{old_dir}", f"{root}/{new_dir}")

    for old_file in files:
        new_file = old_file.replace(args.old, args.new)
        rename(f"{root}/{old_file}", f"{root}/{new_file}")
