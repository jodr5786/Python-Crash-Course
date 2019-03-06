filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    new_lines = ''
    for line in lines:
        new_lines += line.replace('Python', 'PowerShell')

print(new_lines)        