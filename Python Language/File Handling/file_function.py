def create_newfile():
    print("Creating a new file: ")
    file_name = input("\nEnter file name: ")
    file_content = input("\nStart typing the contents: ")
    with open(file_name, "w") as file:
        file.write(file_content)
        file.close()
    print("File written successfully")

def read_mode():
    print("Opening file in read mode")
    file_name = input("\nEnter file name: ")
    print("The file contents are as follows: ")
    print("------------------------------------")
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
        file.close()
    print("---------End of File-----------")

def append_mode():
    file_name = input("\nEnter file name: ")
    file_content = input("\nStart typing the contents: ")
    with open(file_name, "a") as file:
        file.write(file_content)
        file.close()
    print("File written successfully")

while(True):
    print("Menu: ")
    print("1. Create a new file and write")
    print("2. Reopen file in read mode and displayy content")
    print("3. Reopen file in append mode and write into it")
    print("4. Exit")
    print("******************************************************************")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        create_newfile()
    elif ch == 2:
        read_mode()
    elif ch == 3:
        append_mode()
    elif ch == 4:
        break
    else:
        print("Wrong choice! Try again")


print("Exiting the program...")
