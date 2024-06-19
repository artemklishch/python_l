from pathlib import Path

file_path = Path('test.txt')

# print([m for m in dir(file_path) if not m.startswith('_')])

print(Path.cwd())  # /home/artem/development/studing/python_l/45files/pr2

print(Path('usr').joinpath('local').joinpath('bin'))  # usr/local/bin

print(Path('usr') / 'local' / 'bin')  # usr/local/bin

print(Path('main.py').exists())  # True

print(Path('/home/artem/development/studing/python_l/45files/pr2').exists())  # True

print(Path('main.py').is_file())  # True
print(Path('main.py').is_dir())  # False

for f in Path('.').iterdir():
    print(f)
