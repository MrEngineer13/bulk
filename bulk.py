# import libraries
import os

# traverse files and print them
def traverse(folder_path):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            print("[+] Finded file: '" + name + "' at subpath '" + path + "'")
        for name in subdirs:
            print("[+] Finded folder: " + name + "' at subpath '" + path + "'")
traverse(".")