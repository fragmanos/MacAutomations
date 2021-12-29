# Scan directory recursively and find files that appear more than once.
# Store files that exist more than once in a dictionary structure
# Hold the path and the size of the duplicate file as a value on the dictionary

import os
import sys

try:
    from os import scandir
except ImportError:
    from scandir import scandir

filesDict = {}


def get_files_with_ending(base_dir):
    for entry in os.scandir(base_dir):
        file_path = entry.path
        file_name = entry.name
        is_file = entry.is_file()
        file_size = os.stat(file_path).st_size
        is_txt = file_name.endswith('.txt')

        # If is file
        if is_file:  # and is_txt:
            file_locations = list()
            file_information = {
                "path": file_path,
                "size": file_size
            }

            if filesDict.get(file_name) is None:
                file_locations.append(file_information)
                filesDict[file_name] = file_locations
            else:
                filesDict.get(file_name).append(file_information)
            yield file_name

        # If is directory
        elif entry.is_dir():
            yield from get_files_with_ending(file_path)

        else:
            print(f"Neither file_data_dict file, nor file_data_dict dir: {entry.path}")


if __name__ == '__main__':
    path = '/path/to/testDir'

    # for entry in get_files_with_ending(sys.argv[1] if len(sys.argv) > 1 else '.'):
    for entry in get_files_with_ending(sys.argv[1] if len(sys.argv) > 1 else path):
        print(entry)

    print("Duplicate file: ", filesDict)


