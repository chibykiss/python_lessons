import os
# r = Read a file
# a = Append to a file
# w = Write to a file (overwrites existing content)
# x = Create a new file (fails if the file already exists)

f = open('names.txt', 'r')
#print(f.read())
#print(f.read(5))  # Read the first 5 characters
#print(f.readline())  # Read the first line
#print(f.readlines())  # Read all lines into a list
#f.close()

# for line in f:
#     print(line)

# f.close()

# try:
#     f = open('names.txt')
#     print(f.read())
# except FileNotFoundError:
#     print('File not found. Please check the file name and path.')
# finally:
#     f.close()

# Appending to a file
f = open('names.txt', 'a')
f.write('\nTommy')
f.close()

f = open('names.txt', 'r')
print(f.read())
f.close()

# Writing to a file (overwriting existing content)
f = open('context.txt', 'w')
f.write('I deleted all of its content.')
f.close()

f = open('context.txt', 'r')
print(f.read())
f.close()

# Creating a new file two ways

# open a file in write mode, creating it if it doesn't exist
f = open('name_list.txt', 'w')
f.close()

# creates a new file, but returns an error if the file already exists
if not os.path.exists('vibe.txt'):
    f = open('vibe.txt', 'x')
    f.close()
else:
    print('File already exists. Cannot create a new file with the same name.')

#delete a file
if os.path.exists('vibe.txt'):
    os.remove('vibe.txt')
    print('File deleted successfully.')
else:
    print('File does not exist. Cannot delete a file that does not exist.')

# Renaming a file
if os.path.exists('name_list.txt'):
    os.rename('name_list.txt', 'renamed_name_list.txt')
    print('File renamed successfully.')
else:
    print('File does not exist. Cannot rename a file that does not exist.')

# delete entries in a file
with open('names.txt', 'r') as f:
    lines = f.readlines()

lines = [line for line in lines if line.strip() != 'Tommy']  # Remove 'Tommy' from the list

with open('names.txt', 'w') as f:
    f.writelines(lines)

# uisng with statement to handle files
with open('more_names.txt', 'r') as f:
    content = f.read()
    #print(content)

with open('names.txt', 'w') as f:
    f.write(content)