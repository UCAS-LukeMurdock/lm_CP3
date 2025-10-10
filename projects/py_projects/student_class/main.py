# LM  Student Class Project
import csv
# from file_handler import int_input


# def int_input(prompt, min = -1, max = -1): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
#     try:
#         response = int(input(prompt).strip())
#     except:
#         print("Not An Integer")
#         response = int_input(prompt,min,max)
#     if (min != -1 or max != -1) and (response < min or response > max): # If either min or max aren't -1 and the input is out of range then the user has to reinput
#         print(f"Not In Range: {min}-{max}")
#         response = int_input(prompt,min,max)
#     return response

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome, where you can see, add, remove, or search through it.")
    while True:
        choice = int_input("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 1,6)
        if choice == 1:
            ()
        elif choice == 2:
            ()
        elif choice == 3:
            ()
        elif choice == 4:
            ()
        elif choice == 5:
            ()
        elif choice == 6:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
menu()

"""
Write a program that uses a class to abstract a student. Students need to have a student id, name, and grade. The student class should have an __init__ method to initialize the values. Have the id default to 000, name to John Doe and grade to 100. Make a getter function that will display the student's grade. Make a setter function that will change the student's grade. Create at least 5 student objects. Print each object (note that means you will need a __str__ method), change the grades of at least 3 students and then use the getter method to display the new grades. 

OUTPUT EXAMPLE: 
    Inital student info:

    Updated

KEY REMINDERS:
    Use a class to define the Student object with attributes for id, name, and grade.
    Implement the init method with default values for all attributes.
    Create a getter method (get_grade()) to retrieve the student's grade.
    Create a setter method (set_grade()) to modify the student's grade.
    Include a str method for proper string representation of Student objects.
    Create at least 5 Student objects, some with custom values and some with defaults.
    Print all Student objects to demonstrate the str method's functionality.
    Use the setter method to change grades for at least 3 students.
    Use the getter method to display the updated grades after changes.
    Pay attention to proper Python syntax, including correct indentation and method definitions.
    Test the class thoroughly to ensure all required functionality works as expected.
    Use meaningful variable and method names for code clarity.
    Add comments to explain code logic where necessary.
    """