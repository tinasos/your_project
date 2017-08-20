# PROGRAM FileReader4
PathName = "/Users/tinasosiak/Documents/"
NameOfFile = str(input("what File would you like to read:"))
Extension = ".txt"
FullFileName = PathName + NameOfFile + Extension
NumberOfChars = int(input("How many characters: "))

file_pointer = open(FullFileName, "r")
print(file_pointer.read(NumberOfChars))
file_pointer.close()
