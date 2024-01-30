"Start a data analytics project"

import pathlib
import math
import statistics
import os
import econest_utils


def create_project_directory(directory_name:str):   #add type hinting to params
    """Creates a project sub_directory.
    :param directory_name: Name of the directory to be created, e.g. "test"
    """

    pathlib.Path(directory_name).mkdir(exist_ok=True)
    from pathlib import Path
def create_file_or_directory(file_or_directory_name:str):   #add type hinting to params
    path=Path(file_or_directory_name)
    path.touch(exist_ok=True)
    if '/' in file_or_directory_name:
        path.parent.mkdir(exist_ok=True)
        path.touch(exist_ok=True)   
    elif '\\' in file_or_directory_name:
        path.parent.mkdir(exist_ok=True)
        path.touch(exist_ok=True)   
    else:
        path.touch(exist_ok=True)
        #Create a directory
        if not path.exists():
            path.mkdir(exist_ok=True)
            print (f"Directory {file_or_directory_name} created")   
        else:
            print (f"Directory {file_or_directory_name} already exists")

    for year in range (2016, 2023):
        print(year)
def create_annual_data_directories(directory_name, start_year, end_year):
    for year in range(start_year, end_year):
        path = Path(directory_name) / str(year)
        path.touch(exist_ok=True)
        if not path.exists():
            path.mkdir(exist_ok=True)
            print(f"Directory {path} created")
        else:
            print(f"Directory {path} already exists")



def main():
    """Scaffold a project"""
    create_project_directory: str('test')
    create_project_directory: str('docs')


if __name__ == '__main__':
    main()
