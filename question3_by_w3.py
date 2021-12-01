# 3. Write a Python program to append text to a file and display the text.


my_file=open("question_file3.txt","a")
my_file.write("\nI'm doing append hare")
my_file.close
my_file=open("question_file3.txt","r")
print(my_file.read())