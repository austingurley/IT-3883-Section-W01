# Program Name: IT 3883 - Assignment1.py
# Course: IT3883/Section W01
# Student Name: Austin Gurley
# Assignment Number: Lab#1
# Due Date: 09/22/2026
# Purpose: This program displays a text-based menu that lets the user
#          build up a text buffer over time. The user can append strings
#          to the buffer, clear the buffer, display the current buffer
#          contents, or exit the program. The menu loops until the user
#          chooses to exit.
# Resources Used: Python 3 official documentation (input(), while loops, string concatenation).          


def display_menu():
    """Print the four menu options to the screen."""
    print("\n===== MENU =====")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")


def main():
    # The input buffer starts empty and holds all appended text.
    input_buffer = ""

    # Loop the menu until the user chooses option 4, Exit.
    while True:
        display_menu()

        # Prompt the user for a menu choice.
        choice = input("Enter your choice (1-4): ")

        # Option 1: Append data to the input buffer.
        if choice == "1":
            new_data = input("Enter a string to append: ")
            # Connect the new string onto whatever is already stored.
            input_buffer += new_data
            print("Data appended to the buffer.")

        # Option 2: Clear the input buffer.
        elif choice == "2":
            # Reset the buffer back to an empty string.
            input_buffer = ""
            print("The input buffer has been cleared.")

        # Option 3: Display the input buffer.
        elif choice == "3":
            # Show the current contents of the buffer.
            print("Current input buffer:")
            print(input_buffer)

        # Option 4: Exit the program.
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            # Break out of the while loop to end the program.
            break

        # Handle any input that is not 1, 2, 3, or 4.
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()