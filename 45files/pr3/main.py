from os import path
from pathlib import Path

print(path.curdir)
print(path.abspath('.'))

my_dir = Path('.') / 'django'
if not my_dir.exists():
    my_dir.mkdir()

# if my_dir.exists():
#     my_dir.rmdir()

