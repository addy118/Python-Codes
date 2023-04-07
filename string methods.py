name = "Addy"
wrongName = "Teddy"
myName = "my name is Aditya!!!"
ID = "Addy118"
myID = "my ID is Addy118"
spaceName = " Aditya "
greet = "Hello \nAditya"
spaces = "      "
spaces1 = "   1   "

'''
# upper() makes the whole string in uppercase
print(name.upper())

# lower() makes the whole string in lowercase
print(name.lower())

# strip() removes the whitespaces that are before and after the string
print(spaceName.strip())

# rstrip() removes the trailing characters from the string
print(myName.rstrip("!")) # the trailing char needs to be specified in " "

# replace() replaces the string value from one to another
print(wrongName.replace("Te", "A"))

# split() splits and stores the string in a list format (elements divided by spaces in string)
print(myName.split())

# capitalize() makes the first letter of the string capital
print(myName.capitalize())

# title() makes the first letter of every word of the string capital
print(myName.title())

# center() adds half the number of characters instructed to both of the sides of the string
print(name.center(50))
print(name.center(50, "-"))

# count() counts the number of times a character has occured
print(myName.count("a"))

# endswith() checks whether the string ends with the specific character/string or not
print(myID.endswith("18"))
print(myID.endswith("18", 3, 6))
print(myID.endswith("D ", 3, 6))

# startswith() checks whether the string starts with the specific character/string or not
print(myID.startswith("my"))
print(myID.startswith("ID", 3, 6))
print(myID.startswith("dy", 3, 6))

# find() finds the character/string in the string, if true returns index & if false returns -1
print(myID.find("18"))
print(myName.find("18")) # finds 1's index which is before 8

# index() finds the index number of the specific character and throws error if false
print(myID.index("8"))
print(myID.index("1")) # finds 1's index which is before 18
# print(myName.index("18")) # throws an error

# swapcase() swaps the uppercase to lowercase and vice-versa in the string
print(myName.swapcase())

# isalnum() checks whether the string contains alpha-numeric characters, throws error if special char
print(myID.isalnum()) # identifies 'space' as non-alpha-numberic
print(ID.isalnum())

# isalpha() checks whether the string contains alphabets, throws error if numbers, special char
print(name.isalpha())
print(ID.isalpha())

# islower() checks whether the string is in lowercase or not
print(myName.islower())

# isupper() chekcs whether the string is in uppercase or not
print(myID.isupper())

# isprintable() checks whether the string is printable or not, escape seq = non-printable
print(greet.isprintable())
print(myName.isprintable())

# istitle() checks whether the first letter of every word in the string is capital or not
print(greet.istitle())
print(myName.istitle())
print(name.istitle())

# isspace() checks whether the string has 'ONLY SPACES' or not
print(name.isspace())
print(myName.isspace())
print(spaces.isspace())
print(spaces1.isspace())
'''

