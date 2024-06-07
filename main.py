import os
import shutil
import time

file_types = ['.txt', '.pdf', '.docx', '.jpg', '.png', '.mp3', '.mp4', '.xlsx', '.pptx',
              '.zip', '.html', '.css', '.js', '.json', '.csv', '.xml', '.gif', '.wav',
              '.avi', '.php', '.exe', '.dll', '.log', '.bat', '.py', '.java', '.cpp',
              '.h', '.c', '.ini', '.aac', '.aspx']

# Get the path to the user's home directory
home_dir = os.path.expanduser('~')

# Specify the folder to monitor
folder = input("Enter Folder Name: ")
# Construct the path to the specified directory
downloads_dir = os.path.join(home_dir, folder)

# Create a dictionary to store the last modified time for each file
last_modified_times = {file_type: None for file_type in file_types}

while True:
    # List files in the specified directory
    files_in_directory = os.listdir(downloads_dir)
    
    # Loop through each file in the directory
    for file in files_in_directory:
        # Check if the file is of one of the specified types
        for file_type in file_types:
            if file.endswith(file_type):
                src_file = os.path.join(downloads_dir, file)
                # Get the last modified time for the file
                last_modified_time = os.path.getmtime(src_file)
                
                # Check if the file has been modified since last check
                if last_modified_time != last_modified_times[file_type]:
                    # Update the last modified time for the file type
                    last_modified_times[file_type] = last_modified_time
                    
                    # Create folder for the file type if it doesn't exist
                    dst_folder = os.path.join(downloads_dir, file_type[1:])
                    if not os.path.exists(dst_folder):
                        os.makedirs(dst_folder)
                    
                    # Move the file to the corresponding folder and rename it
                    idx = len(os.listdir(dst_folder)) + 1
                    dst_file = os.path.join(dst_folder, f"{idx}{file_type}")
                    shutil.move(src_file, dst_file)
                    print(f"File {file} moved to {dst_folder} and renamed to {idx}{file_type}")
                    
                    # Exit the loop after processing the file
                    break
    
    # Wait for some time before checking again
    time.sleep(5)  # Adjust the interval as needed
