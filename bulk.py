#!/usr/bin/env python3
# import libraries
import argparse
import os
import re


# modify filename
def rename_convension(filename, replace, replacement):

    # replace name
    modified = filename
    modified = modified.replace(replace, replacement)

    # remove paranthese and text between them
    modified = re.sub(r'\([^)]*\)', '', modified)
    modified = re.sub(r'\[[^)]*\]', '', modified)

    # replace double spaces and space before dot
    modified = modified.replace("  ", " ").replace(" .", ".")
    
    # return 
    return modified

# traverse files and print them
def traverse(
        folder_path,
        replace,
        replacement,
        recursive=False,
        exceptions=tuple(),
        only=None,
        script_name=__file__,
):

    for path, subdirs, files in os.walk(folder_path):

        # recursive
        if recursive or ((not recursive) and (path == folder_path)):

            # files
            if (not only) or (only == "files"):

                for name in files:

                     # verify if file is script
                    if name == script_name:
                        # @TODO: here is might be a case with a same filename
                        # subdirectories might contain files with such names
                        continue

                    # exception break
                    flag = False
                    if exceptions:
                        extension = os.path.splitext(name)[1][1:]
                        for ext in exceptions:
                            if extension == ext:
                                flag = True
                                break
                    if not flag:
                        print("[+] Renaming file '" + name + "'(from subpath '" + path + "') as '" + rename_convension(name,replace,replacement) + "'")
                        file_path = os.path.join(path, name)
                        new_name = os.path.join(path, rename_convension(name,replace,replacement))
                        os.rename(file_path, new_name)

            # folders
            if (not only) or (only == "folders"):
                for name in subdirs:
                        print("[+] Renaming folder '" + name + "'(from subpath '" + path + "') as '" + rename_convension(name,replace,replacement) + "'")
                        file_path = os.path.join(path, name)
                        new_name = os.path.join(path, rename_convension(name,replace,replacement))
                        os.rename(file_path, new_name)
                        name = rename_convension(name,replace,replacement)

# main
if __name__ == "__main__":

    # set arguments
    parser = argparse.ArgumentParser(
        description='Bulk rename files and folder from PATH',
        epilog='Example of usage: ./bulk.py ./website  oldname newname -r -e html css js -o files',
        add_help=True,
    )
    parser.add_argument('path', action="store", nargs="*", default=True,
                        help='*REQUIRED* path to a directory with files')
    parser.add_argument('replace', action="store", nargs="*", default=True,
                        help='*REQUIRED* name to replace')
    parser.add_argument('replacement', action="store", nargs="*", default=True,
                        help='*REQUIRED* replaced name')
    parser.add_argument('-e', '--exceptions', action="store", nargs="*", default=False,
                        help='Except from renaming given extensions')
    parser.add_argument('-r', '--recursive', action="store_true", default=False,
                        help='Recursive enter in folders')
    parser.add_argument('-o', '--only', action="store", default=False, choices=['files', 'folders'],
                        help='Apply renaming only on files/folders')
    args = parser.parse_args()

    if hasattr(args, 'path') and isinstance(args.path, list):
        script_name = __file__.lstrip('.').lstrip('/')
        traverse(args.path[0], args.path[1], args.path[2], args.recursive, args.exceptions, args.only,
                 script_name=script_name)
    else:
        parser.print_help()
        exit(1)
