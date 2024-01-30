''' This module provides functions for creating a series of project folders. '''
import math
import statistics
import econest_utils
import pathlib
import os
import time




def create_folders_for_range(start, end):
        """Create a series of project folders from start to end."""
        for i in range(start_year, end_year+1):
            folder_name = f"project_{i}"
            os.makedirs(folder_name, exist_ok=True)
def create_folders_from_list(folder_names, to_lowercase=False, remove_spaces=False):
      """
      Creates folders from a list of folder names.
      """
      for folder_name in folder_names:
          if to_lowercase:
              folder_name = folder_name.lower()
          if remove_spaces:
              folder_name = folder_name.replace(" ", "")
          os.makedirs(folder_name, exist_ok=True)
def create_prefixed_folders(folder_list,prefix):
     """
     Creates prefixed folders from a list of folder names in the current working directory.
     :param folder_list: list of folder names, e.g., ['Chicken', 'Sheep', Ducks']
     :param prefix: prefix to be added to each folder name, e.g., 'Animal_' or 'Food_'
     :return:
     """
     # Using list comprehension to create prefixed folders
     folders = [pathlib.Path(f"{prefix}{name}") for name in folder_list]
    
    # Creating the folders in the current working directory
     for folder in folders:
          new_func(folder)

def new_func(folder):
   import pathlib
   
   def create_folder(folder_path):
       pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
def create_folders_periodically(delay_seconds):
     """Creates folders periodically.
    :param prefix:  Prefix to be added to each folder name, e.g., 'Animal_' or 'Food_'
    :param num_folders: Number of folders to be created
    :param delay_seconds: Delay between each folder (5 seconds by default)
    """
     
     num_folders = 5 # Number of folders to be created
     next_file = 1 # Int to start while loop

     while next_file <= num_folders:
          pathlib.Path("folder_" + str(next_file)).mkdir(exist_ok=True)
          next_file += 1
          time.sleep(delay_seconds)

def main():
     """Main function to demonstrate module capabilities."""
     # Print byline from imported module
     print(f"Byline: {econest_utils.byline}")

     # Call function 1 to create folders for a range (e.g. years)
     create_folders_for_range(start_year=2015, end_year=2020)

     # Call function 2 to create folders from a list
     folder_names = ['Chicken', 'Sheep', 'Ducks']
     create_folders_from_list(folder_names)

     # Call function 3 to create prefixed folders
     folder_names = ['Chicken', 'Sheep', 'Ducks']
     prefix = 'Animal_'
     create_prefixed_folders(folder_names, prefix)

     # Call function 4 to create folders periodically
     create_folders_periodically(delay_seconds=5)

     # Add options e.g. to force lowercase and remove spaces 
     # to one or more of your functions (see above for examples)
     regions = [
          "North America",
          "South America",
          "Europe",
          "Asia",
          "Africa",
          "Oceania",
          "Middle East",
     ]
     create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)


if __name__ == "__main__":
     main()
