
my_file=open("question6_file.txt","r")
read=my_file.read()
my_file2=open("question6_delhi.txt","w")
my_file3=open("question6_shimla.txt","w")
my_file4=open("question6_others.txt","w")
file_data=read.split("\n")
print(file_data)
i=0
while i<len(file_data):
    if "delhi" in file_data[i]:
        my_file2.write(file_data[i])
        my_file2.write("\n")
    elif "shimla" in file_data[i]:
        my_file3.write(file_data[i])
        my_file3.write("\n")
    else:
        my_file4.write(file_data[i])
        my_file4.write("\n")
    i+=1