# LM  Student Class Project


class Student: # Class of a Student
    def __init__(self, id = 0, name = "John Doe", grade = 100): # Intializes attributes and had default ones if needed
        self.id = id
        self.name = name
        self.grade = grade
    
    def __str__(self): # Displays student info if the object is printed
        return f"Student ID: {self.id} | Name: {self.name} | Grade: {self.grade}"
    
    def get_grade(self): # Displays the student's grade
        return f"{self.name}'s Grade: {self.grade}"
    
    def set_grade(self): # It increases the student's grade by 1, and if it is below 0 it will become 0, even though that is impossible.
        self.grade += 1
        if self.grade < 0:
            self.grade = 0


def program(): # Makes student objects, displays their info, updates some of their grades, and displays those updated grades
    normal = Student()
    george = Student(1, "George Bob", 52)
    bobby = Student(2, "Bobby Joe")
    luke = Student(3, "Luke Murdock", 99)
    nick = Student(4, "Nick Larsen", 0)

    print(f"\nIntial Student Information:\n{normal}\n{george}\n{bobby}\n{luke}\n{nick}")

    normal.set_grade()
    luke.set_grade()
    nick.set_grade()

    print(f"\nUpdated grades:\n{normal.get_grade()}\n{luke.get_grade()}\n{nick.get_grade()}")


def menu(): # Introduces the program and then lets the user choose to keep going or exit
    print("\n\nWelcome to this Student Informaion Program, where you can see the student information and the their updated grades.")
    
    while True:
        choice = input("\nDisplay(1) Exit(2)\nChoice: ")
        if choice == "1":
            program()

        elif choice == "2":
            print("\n\n\nCome Back Soon!\n\n\n")
            break

        else:
            print("\nInvalid Input! (Enter a number 1-2)")

menu()



"""
INSTRUCTIONS:
    Write a program that uses a class to abstract a student. Students need to have a student id, name, and grade.
    The student class should have an __init__ method to initialize the values.
    Have the id default to 000, name to John Doe and grade to 100.
    Make a getter function that will display the student's grade.
    Make a setter function that will change the student's grade.
    Create at least 5 student objects.
    Print each object (note that means you will need a __str__ method), change the grades of at least 3 students and then use the getter method to display the new grades. 

OUTPUT EXAMPLE: 
    Inital student info:

    Updated:

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