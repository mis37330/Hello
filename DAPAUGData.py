output = "AUGDAPDataCorrection.txt"
file1 = open("C:\\Users\\M\\Desktop\\Coding\\AUGDAPData.txt", "r")
file2 = open("C:\\Users\\M\\Documents\\AUGDAPDataCorrection.txt", "w")
for x in file1:
    a_string = x;
    isnumeric = "\n"

    for character in a_string:
        if character.isnumeric():
            isnumeric += character
print(isnumeric)
file2.write(isnumeric)

file2.close()
file.close()