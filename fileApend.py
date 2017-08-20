#PROGRAM FileWrite5
#program wite to the start of the file
file_pointer = open("/Users/tinasosiak/Documents/number.txt", "r+"
Current_file = file_pointer.read()
New_file = "Start of file\n" + Current_file

file_pointer.seek(0) 
file_pointer.write(New_file)
File_pointer.colose
