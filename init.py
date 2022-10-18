import os


username = input("enter username >> ")
password = input("enter password >> ")

with open(".env", "w") as f:
    f.write("usr=" + username)
    f.write("\n")
    f.write("pswd=" + password)

