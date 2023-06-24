import zipfile
import pathlib
def make_zip(file,folder):
    dest_folder=pathlib.Path(folder,"Compressed.zip")
    with zipfile.ZipFile(dest_folder,'w') as archive:
        for filepath in file:
            filepath=pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)