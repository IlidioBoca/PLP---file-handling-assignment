def file_read_write():
    """Reads a file, modifies the content, and writes it to a new file."""
    try:
      
        with open("input.txt", "r", encoding="utf-8") as f:
            content = f.readlines()
       
        modified_content = [f"{i+1}: {line.upper()}" for i, line in enumerate(content)]

        with open("output.txt", "w", encoding="utf-8") as f:
            f.writelines(modified_content)

        print("\n File successfully modified! Check 'output.txt'.\n")

    except FileNotFoundError:
        print("\n Error: The file 'input.txt' was not found.\n")
#--------------------------------------------------------------------------------------------------

def error_handling_lab():
    """Asks the user for a filename and tries to open it with error handling."""
    filename = input("\nEnter the filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("\n--- File Content ---")
            print(content)

    except FileNotFoundError:
        print("\n Error: The file does not exist.\n")
    except PermissionError:
        print("\n Error: You don’t have permission to read this file.\n")
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}\n")


def menu():
    """Main menu to select challenges."""
    while True:
        print("=== File Handling and Exception Handling Assignment ===")
        print("1. File Read & Write Challenge")
        print("2. Error Handling Lab")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            file_read_write()
        elif choice == "2":
            error_handling_lab()
        elif choice == "3":
            print("\n Program ended. Goodbye!\n")
            break
        else:
            print("\n Invalid option! Please try again.\n")


if __name__ == "__main__":
    menu()
