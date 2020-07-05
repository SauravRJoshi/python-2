filename =  input("Enter a file name whose extension is only three letters : ")
file_extension = filename[-3:]
new_name = filename[:-4]

print("The new name is",new_name)
print("The extension found was",file_extension)