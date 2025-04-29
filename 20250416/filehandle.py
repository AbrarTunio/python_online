
# filehandle = open("content.txt" , "r" )
# print( filehandle.readlines() )

# with open("content.txt" , "r") as fh:
#  print(fh.read())

# with open("content.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# with open("content.txt", "w") as file:
#     file.write("Hello, World!\n")

# with open("content.txt", "a") as file:
#     file.write("Appending new data.\n")
#     file.write("Awesome filehandling is fun!.\n")


# with open("content.txt" , "r") as fh:
#  print(fh.read())


# try:
#     with open("somefile.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("File not found!")

# with open("somefile.txt", "r") as file:
#        content = file.read()

# with open("myfile.txt", "w") as file:
#     file.write("This is a sample text written to a new file.")

with open("myfile.txt", "r") as file:
    content = file.read()
    print( type(content) )
    words = content.split()
    print( type(words) )
    print(f"Total words: {len(words)}")
    print((words))
