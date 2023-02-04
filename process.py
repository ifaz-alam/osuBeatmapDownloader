import hashlib
import os

# Directory containing the files
directory = r"D:\Users\Admin\AppData\Local\osu!\Songs"

# Get a list of all the folders in the directory
folders = os.listdir(directory)

# Iterate through the list of folders
for folder in folders:
  folder_path = os.path.join(directory, folder)

  # Get a list of all the .osu files in the folder
  files = [file for file in os.listdir(folder_path) if file.endswith('.osu')]

  # Iterate through the list of .osu files
  for file in files:
    file_path = os.path.join(folder_path, file)

    # Create a new MD5 hash object
    hash_obj = hashlib.md5()

    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        """
        The update() method is used to feed data to the hash function in chunks, rather than reading the entire file into memory at once.
        This can be useful if you are dealing with very large files that might not fit in memory. Here is an alternative way we could have written the code below.
        It is not necessary in this case because .osu files are not very large.

        # Read the file in chunks and update the hash object
        chunk = f.read(1024)
        while chunk:
            hash_obj.update(chunk)
            chunk = f.read(1024)

        # Get the hexadecimal representation of the hash
        hash = hash_obj.hexdigest()

        # Print the file name and the hash
        print(f'{file}: {hash}')
        """
        try:
            # Read the contents of the file
            contents = f.read()

            # Compute the MD5 hash of the contents
            hash = hashlib.md5(contents).hexdigest()

            # Print the file name and the hash
            print(f'{file}: {hash}')
        except:
            print(f'Could not decrypt the file with the hash {hash}')