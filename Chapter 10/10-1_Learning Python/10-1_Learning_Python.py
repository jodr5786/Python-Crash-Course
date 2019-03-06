filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print()

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

print()

with open(filename) as f:
    contents = f.read()
print(contents)