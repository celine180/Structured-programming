"""
This is a simple program that allows the user to add items to a list, view the items in the list, and exit the program. 
The program uses a while loop to keep running until the user chooses to exit. 
It also includes error handling to manage invalid inputs and unexpected errors.
"""


items = [] #list to store items
while True: #infinite loop to keep the program running until the user chooses to exit
    try: #try block to catch any exceptions that may occur during the execution of the code
       print("\n Menu ")
       print("1. Add")
       print("2. View")
       print("3. Exit")

       your_choice = input("Choose an option (1, 2, 3): ")
       
       match your_choice:
          case "1":
             try:
                item = input("Enter item: ").strip()
                if not item: #checks if the input is empty and raises a ValueError if it is
                   raise ValueError("Item cannot be empty") 
                items.append(item)
                print(f" {item} has been added.")
             except ValueError as e: #handles the ValueError raised when the input is empty
                print (f"Error: {e}")

          case "2":
             print("\n Your items: ")
             if not items: #checks if the list is empty and prints a message if it is
              print("List is empty")
             else:
              for index, item in enumerate(items, start=1): #enumerate is used to get the index of the item in the list, starting from 1
               print(f"{index}. {item}")
          case "3":
            print("Exit. Bye")
            break #exits the loop and ends the program

          case _: #handles any other input that is not 1, 2 or 3 and prints an error message
           print("Invalid choice. Please enter 1, 2 or 3")
    except KeyboardInterrupt: #prevents the program from crashing when ctrl+c is pressed
      print("\nProgram interrupted. Exiting safely")
      break
    except EOFError: #prevents the program from crashing when ctrl+d is pressed
      print("\nNo input received. Exiting")
      break
    except Exception as e: #handles any other unexpected errors
      print(f"An unexpected error occured: {e}")
