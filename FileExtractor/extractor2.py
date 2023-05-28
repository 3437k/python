import os
import re  # regex
import shutil  # file copy or move

# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape 
# convert string to raw string, (\\, escape sequence) to (\)
base_path = r"C:\Users\ryan\Downloads\pictures\2023"

# files or folder list, ['001.JPG', '2019-01']
base_list = os.listdir(base_path)

for base_item in base_list:
    # extract year-month-day, 2023-05-28
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', base_item)

    # Not None
    if match:
        target_path = os.path.join(base_path, base_item)
        source_list = os.listdir(target_path)

        year = match.group(1)
        month = match.group(2)
        day = match.group(3)

        year_month = f"{year}-{month}"
        destination_folder = os.path.join(base_path, year_month)

        # Create folder
        os.makedirs(destination_folder, exist_ok=True)

        for source_item in source_list:
            # file path
            source_file_path = os.path.join(target_path, source_item)

            destination_file_name = f"{year}-{month}-{day}-{source_item}"
            
            destination_file_path = os.path.join(destination_folder, destination_file_name)

            # Check duplicate files
            if os.path.exists(destination_file_path):
                base_name, extension = os.path.splitext(destination_file_name)
                i = 1
                while True:
                    # Change to another name
                    new_destination_file_name = f"{base_name}_{i}{extension}"
                    new_destination_file_path = os.path.join(destination_folder, new_destination_file_name)
                    if not os.path.exists(new_destination_file_path):
                        destination_file_path = new_destination_file_path
                        break
                    i += 1

            # Move
            shutil.move(source_file_path, destination_file_path)
