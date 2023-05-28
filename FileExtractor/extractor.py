import os
import shutil

# Customize folder path or name
source_folder = "./targets"
target_name = "_en_"
target_folder = "./targets/copied"

fileCount = 0

if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    
# If not folder, create folder
if not os.path.exists(target_folder) and len(os.listdir(source_folder)) > 0:    
    os.makedirs(target_folder)

    for filename in os.listdir(source_folder):            
        if target_name in filename:                            
            source_path = os.path.join(source_folder, filename)                        
            destination_path = os.path.join(target_folder, filename)
            
            # Copy!
            shutil.copy(source_path, destination_path)         

            # Print filename
            print (filename);
            fileCount += 1

print(f"{fileCount} files have been copied.")
