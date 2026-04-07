import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File {filename} not fount")

def write_file(filename,content):
        with open(filename, 'w') as file:
            file.write(content)
            print(f" Content written to {filename}")

def append_file(filename,content):
        with open(filename, 'a') as file:
            file.write(content + "\n")
            print(f" Content Append to {filename}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} Deleted!")
    except FileNotFoundError:
        print(f"File {filename} not found")


def main():

    while True:
        print("File Operation")
        print("1. Read File")
        print("2. Write File")
        print("3. Append File")
        print("4. Delete File")
        print("5. Exit")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid Choice")

        if choice == 1:
            filename = input("Enter Filename: ")
            read_file(filename)
        elif choice == 2:
            filename = input("Enter Filename: ")
            content = input("Enter Content")
            write_file(filename,content)
        elif choice == 3:
            filename = input("Enter Filename: ")
            content = input("Enter Content")
            append_file(filename,content)
        elif choice == 4:
            filename = input("Enter Filename")
            delete_file(filename)
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Invalid Option")

main()        