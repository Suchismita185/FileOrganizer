"""
File Organizer
--------------
Organizes files in a target directory into subfolders based on
their file extensions.

Features:
1. Accepts a directory path from the command line or user input.
2. Creates a separate folder for each file extension.
3. Moves files into their corresponding folders.
4. Prevents overwriting existing files by adding numeric suffixes.
5. Handles errors and displays clear status messages.
6. Uses only Python standard library modules.

Example:
    Before:
        Downloads/
        ├── photo.jpg
        ├── document.pdf
        ├── script.py
        └── notes.txt

    After:
        Downloads/
        ├── jpg/
        │   └── photo.jpg
        ├── pdf/
        │   └── document.pdf
        ├── py/
        │   └── script.py
        └── txt/
            └── notes.txt
"""

import os
import shutil
import sys


def get_unique_path(destination_folder, filename):
    """
    Generate a destination path that does not overwrite an existing file.

    If a file already exists, append a numeric suffix before its extension.

    Example:
        photo.jpg
        photo_1.jpg
        photo_2.jpg

    Args:
        destination_folder (str): Folder where the file will be moved.
        filename (str): Original filename.

    Returns:
        str: A unique destination path.
    """

    destination_path = os.path.join(destination_folder, filename)

    # If the destination does not exist, use the original filename.
    if not os.path.exists(destination_path):
        return destination_path

    # Separate the filename from its extension.
    name, extension = os.path.splitext(filename)

    counter = 1

    # Find an unused filename by adding a numeric suffix.
    while True:
        new_filename = f"{name}_{counter}{extension}"
        destination_path = os.path.join(
            destination_folder, new_filename
        )

        if not os.path.exists(destination_path):
            return destination_path

        counter += 1


def organize_files(target_directory):
    """
    Organize files in the target directory by their extensions.

    Directories are not moved. Files without an extension are placed
    in a folder named 'no_extension'.

    Args:
        target_directory (str): Directory whose files will be organized.
    """

    # Convert the directory to an absolute path.
    target_directory = os.path.abspath(target_directory)

    # Verify that the directory exists.
    if not os.path.isdir(target_directory):
        print(f"[ERROR] Directory does not exist: {target_directory}")
        return

    print("\n====================================")
    print("        FILE ORGANIZER")
    print("====================================")
    print(f"Target directory: {target_directory}\n")

    moved_count = 0
    skipped_count = 0
    error_count = 0

    try:
        # os.scandir() examines only the immediate contents of the
        # target directory, not its subdirectories recursively.
        with os.scandir(target_directory) as entries:

            for entry in entries:

                try:
                    # Skip directories, symbolic links, and other
                    # entries that are not regular files.
                    if not entry.is_file(follow_symlinks=False):
                        continue

                    filename = entry.name
                    source_path = entry.path

                    # Extract the extension, ignoring the leading dot.
                    # For example: "photo.jpg" -> "jpg"
                    _, extension = os.path.splitext(filename)

                    if extension:
                        folder_name = extension[1:].lower()
                    else:
                        # Files without extensions go into this folder.
                        folder_name = "no_extension"

                    # Create the destination folder if necessary.
                    destination_folder = os.path.join(
                        target_directory, folder_name
                    )

                    # Avoid moving a file into itself.
                    if os.path.abspath(source_path) == os.path.abspath(
                        destination_folder
                    ):
                        print(f"[SKIPPED] {filename}: invalid destination.")
                        skipped_count += 1
                        continue

                    os.makedirs(destination_folder, exist_ok=True)

                    # Generate a unique path to avoid overwriting.
                    destination_path = get_unique_path(
                        destination_folder, filename
                    )

                    # Move the file to its destination folder.
                    shutil.move(source_path, destination_path)

                    print(
                        f"[MOVED] {filename}\n"
                        f"        -> {destination_path}"
                    )

                    moved_count += 1

                except OSError as error:
                    # Handle errors affecting individual files.
                    print(f"[ERROR] Could not process {entry.name}: {error}")
                    error_count += 1

    except OSError as error:
        # Handle errors while reading the target directory.
        print(f"[ERROR] Could not access the directory: {error}")
        return

    # Display a summary of the operation.
    print("\n====================================")
    print("        ORGANIZATION SUMMARY")
    print("====================================")
    print(f"Files moved   : {moved_count}")
    print(f"Files skipped : {skipped_count}")
    print(f"Errors        : {error_count}")
    print("Organization process completed.")
    print("====================================")


def main():
    """
    Main entry point of the program.

    Accepts a directory path as a command-line argument.
    If no argument is supplied, prompts the user to enter a path.
    """

    # Use the first command-line argument if provided.
    if len(sys.argv) > 1:
        target_directory = " ".join(sys.argv[1:]).strip().strip('"')
    else:
        target_directory = input(
            "Enter the directory path to organize: "
        ).strip().strip('"')

    if not target_directory:
        print("[ERROR] No directory path provided.")
        return

    organize_files(target_directory)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
