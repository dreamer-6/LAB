import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to '{filename}'.")

def append_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + "\n")
    print(f"Content appended to '{filename}'.")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def main():
    while True:
        print("\n--- File Operations ---")
        print("1. Read File")
        print("2. Write File")
        print("3. Append File")
        print("4. Delete File")
        print("5. Exit")
      
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue # Skips the rest of the loop and prompts again
        
        if choice == 1:
            filename = input("Enter filename: ")
            read_file(filename)
        elif choice == 2:
            filename = input("Enter filename: ")
            content = input("Enter content: ")
            write_file(filename, content)
        elif choice == 3:
            filename = input("Enter filename: ")
            content = input("Enter content: ")
            append_file(filename, content)
        elif choice == 4:
            filename = input("Enter filename: ")
            delete_file(filename)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()