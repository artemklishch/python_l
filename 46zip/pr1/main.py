from zipfile import ZipFile
from pathlib import Path

# Path('files').mkdir()
#
# with open("files/first.txt", 'w') as my_file:
#     my_file.write("This is first file")
#
# with open("files/second.txt", 'w') as my_file:
#     my_file.write("This is second file")

# with ZipFile('files.zip', mode='w') as my_zip_file:
#     # print(my_zip_file)
#     for file in Path('files').iterdir():
#         print(file)
#         my_zip_file.write(file)


with ZipFile('files.zip') as my_zip_file:
    # my_zip_file.extractall('my-files-unzipped')
    print(my_zip_file.infolist())
    print(my_zip_file.filename)

