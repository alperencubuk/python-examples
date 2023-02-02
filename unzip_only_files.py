import os
import shutil
import zipfile

my_dir = "folder"
my_zip = "zipfile.zip"

# Unzip without structure just files
def unzip(zip_path: str, extract_dir: str):
    with zipfile.ZipFile(zip_path) as zip_file:
        os.makedirs(extract_dir, exist_ok=True)
        for member in zip_file.namelist():
            filename = os.path.basename(member)
            # skip directories
            if not filename:
                continue
            if not member.startswith('__MACOSX'):
                source = zip_file.open(member)
                target = open(os.path.join(extract_dir, filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)

unzip(my_zip, my_dir)