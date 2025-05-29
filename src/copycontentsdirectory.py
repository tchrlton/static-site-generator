import os
import shutil

def copy_contents_directory(src_dir: str, dst_dir: str):
    # Create destination directory if it doesn't exist
    os.makedirs(dst_dir, exist_ok=True)
    
    # Clean out destination directory contents
    for item in os.listdir(dst_dir):
        item_path = os.path.join(dst_dir, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    
    # Copy all items from source to destination
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            copy_contents_directory(src_path, dst_path)