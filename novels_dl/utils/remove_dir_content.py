import os
import shutil


def remove_dir_content(dir_path: str):
    """Recursively removes directory content, without deleting the directory itself"""

    for path in os.listdir(dir_path):
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
