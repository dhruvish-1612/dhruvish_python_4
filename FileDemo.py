file=open("tops1.txt","w")
file.write("this is file management write operation using python.")
file.close()
print("File Written Successfully")
print("*"*60)

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*"*60)

file=open("tops1.txt","a")
file.write("\nNow this is appended")
file.close()
print("*"*60)

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*"*60)

file=open("tops2.txt","w+")
file.write("This is w+ mode using python file management.")
print("Current Cursor Position : ",file.tell())
file.seek(0)
print(file.read())
file.close()
print("*"*60)

file=open("tops2.txt","r+")
file.seek(45)
file.write("\nr+ operation.")
file.seek(0)
print(file.read())
file.close()
print("*"*60)