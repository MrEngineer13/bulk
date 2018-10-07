# bulk

```
Usage: python bulk.py PATH [OPTIONS]
Bulk rename files and folder from PATH

Available options:
-e, --except         Except from renaming given extensions
-r, --recursive      Recursive enter in folders 
-o, --only           Apply renaming only on files/folders
-h, --help           Display this help and exit

Example of usage:
python3 bulk.py ./website -r -e html css js -o files
```