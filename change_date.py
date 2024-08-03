import os
import time


def update_modification_dates_to_now(folder_path):
    """
    Update the modification date of all files in the specified folder to the current date and time.

    Parameters:
    folder_path (str): Path to the folder containing the files.
    """
    current_timestamp = time.time()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.utime(file_path, (current_timestamp, current_timestamp))
            print(f"Updated {file_path} to current date and time")


# Example usage:
folder_path = r'F:\AutoSegVision\lib\net'
update_modification_dates_to_now(folder_path)
