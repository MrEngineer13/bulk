# import libraries
import os
import re

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
def traverse(folder_path):
    for path, subdirs, files in os.walk(folder_path):

        # files
        for name in files:
            print("[+] Finded file: '" + name + "' at subpath '" + path + "' will be renamed as '" + rename_convension(name) + "'")
        
        # folders
        for name in subdirs:
            print("[+] Finded folder: " + name + "' at subpath '" + path + "' will be renamed as '" + rename_convension(name) + "'")

# main
traverse(".")