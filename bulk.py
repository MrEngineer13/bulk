# import libraries
import os
import re
import argparse

# constants
SCRIPT = "bulk.py"

# print help
def help():
    print("Usage: python bulk.py PATH [OPTIONS]")
    print("Bulk rename files and folder from PATH\n")
    print("Available options:")
    print("{0: <20} {1: >20}".format("-e, --except", "Except from renaming given extensions"))
    print("{0: <20} {1: >20}".format("-r, --recursive", "Recursive enter in folders "))
    print("{0: <20} {1: >20}".format("-o, --only", "Apply renaming only on files/folders"))
    print("{0: <20} {1: >20}".format("-h, --help", "Display this help and exit"))
    print("\nExample of usage:")
    print("python bulk.py ./website -r -e html css js -o files")
    exit()

# modify filename
def rename_convension(filename):

    # capitalize only first letter
    modified = filename
    intermediar = list(modified)
    intermediar[0] = intermediar[0].upper()
    modified = "".join(intermediar)

    # remove paranthese and text between them
    modified = re.sub(r'\([^)]*\)', '', modified)
    modified = re.sub(r'\[[^)]*\]', '', modified)

    # replace double spaces and space before dot
    modified = modified.replace("  ", " ").replace(" .", ".")
    
    # return 
    return modified

# traverse files and print them
def traverse(folder_path, recursive=False, exceptions=[], only=None):

    for path, subdirs, files in os.walk(folder_path):

        # recursive
        if recursive or ((not recursive) and (path == folder_path)):

            # files
            if (not only) or (only == "files"):

                for name in files:

                     # verify if file is script
                    if name == SCRIPT:
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
                        print("[+] Finded file: '" + name + "' at subpath '" + path + "' will be renamed as '" + rename_convension(name) + "'")
            
            # folders
            if (not only) or (only == "folders"):
                for name in subdirs:
                        print("[+] Finded folder: " + name + "' at subpath '" + path + "' will be renamed as '" + rename_convension(name) + "'")

# main
if __name__ == "__main__":

    # set arguments
    parser = argparse.ArgumentParser(description='Bulk rename script', add_help=False)
    parser.add_argument('path', action="store", nargs="*", default=True)
    parser.add_argument('-e', '--exceptions', action="store", nargs="*", default=False)
    parser.add_argument('-r', '--recursive', action="store_true", default=False)
    parser.add_argument('-o', '--only', action="store", default=False, choices=['files', 'folders'])
    parser.add_argument('-h', '--help', action="store_true", default=False)
    args = parser.parse_args()
    
    # help
    if args.help:
        help()

    # with path given
    try:
        args.path
    except NameError:
        help()
    traverse(args.path[0], args.recursive, args.exceptions, args.only)