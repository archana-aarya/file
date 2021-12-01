# Write a Python program to read last n lines of a file.

my_file=open("Question_file4.txt","r")
read=my_file.readlines()
stor=read
# my_file.close
i=0
count=0
while i<len(stor):
    count=count+1
    i=i+1
print(count)
my_file.close