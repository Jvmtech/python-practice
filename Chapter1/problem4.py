import os
from tokenize import Comment

"""def list_directory_contents(directory):
    try:
        # Get list of files and directories
        contents = os.listdir(directory)
        
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied.")

# Specify the directory (change this as needed)
directory_path = "../abc"  # Current directory
list_directory_contents(directory_path)

#multiline comment in python"
"""

import os

directory_path ="./ab"
#print("Contents of", os.listdir(directory_path))

try:
    content = os.listdir(directory_path)
    for item in content:
        print(item)
except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")

# create more program
