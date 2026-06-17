file_path = "todolist.txt"

is_active = True

while is_active:
    choice = input(
        "**********************"
        "**********************"
        "**********************"
        "\n1. Add activity\n"
        "2. Remove activity\n"
        "3. Exit\n" 
        "**********************"
        "**********************"
        "**********************\n"
        "Select option: " 
        
    )

    if choice == "1":
        activity = input("Enter activity here: ")

        with open(file_path, "a") as file:
            file.write(activity + "\n")

        print("Done, Master!")

        with open(file_path, "r") as file:
            print(
                
                  file.read()
                )

    elif choice == "2":
        print("Remove feature not implemented yet.")

    elif choice == "3":
        is_active = False

    else:
        print("Invalid choice.")

