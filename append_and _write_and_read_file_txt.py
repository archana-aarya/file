my_file= open("file2.txt", "a")
my_file.write("\nNow the file has more content!")
my_file.close()

#open and read the file after the appending:
my_file= open("file2.txt", "r")
print(my_file.read())