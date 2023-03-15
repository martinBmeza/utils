#!/bin/python
import os
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Replace spaces with underscores and convert uppercase to lowercase in folder names')
args = parser.parse_args()

# Get all folder names in current directory
folders = [f for f in os.listdir() if os.path.isdir(f)]
# Loop through each folder name
for folder in folders:
    # Replace spaces with underscore
    new_folder = folder.replace(' ', '_')

    # Convert uppercase to lowercase
    new_folder = new_folder.lower()

    # Rename folder
    if folder != new_folder:
        os.rename(folder, new_folder)

