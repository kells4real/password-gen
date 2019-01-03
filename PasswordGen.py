import string
from random import *
import pyperclip

print("Password Generator///")
print()

website = input('Enter Website: ')
username = input('Enter Username: ')



characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(12, 16)))
pyperclip.copy(password)

print("password: ", password)
print("The password has been copied to clipboard. You may paste the generated password where you'd like..")

file1 = open("password.txt", "a+") #write
file1.write("Website: ")
file1.write(website)
file1.write(", Username: ")
file1.write(username)
file1.write(', Password: ')
file1.write(password)
file1.write("\n")
file1.write("\n")


file1.close()

