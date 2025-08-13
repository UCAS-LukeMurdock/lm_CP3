# Luke Murdock, Quiz Game
from quiz import take

"""
Create a quiz game that asks the user at least 10 questions (randomly selected from a csv that holds at least 50 questions [yes you can use AI to create your questions and answers]).
Let users answer (they should be multiple choice questions but make sure your user knows what to do to select their choice)
Tell the user if they got the question right or wrong
Give the overall score at the end
The program needs to run until the user selects to quit

MORE CHALLENGES:
Create a user interface with tkinter or turtle that lets users click on the answers they want
|Allow users to select from different lists of questions
|Allow users to create lists of questions
|User profiles (Admin users can create new lists of questions, normal users can just select from lists of questions to do)
Give different point amounts based on how quickly they answer
||Shuffle the order the answers are displayed 
KEY REMINDERS:
CSV's use a csvreader
Think carefully about the data types you want to use!
Make clear user instructions for how they answer questions
Don't forget to plan extra debugging time! You can always add more once you have an MVP!


Submit the link to this project in GitHub (It will have multiple files so I want a link to the project folder!)


Program Properly reads CSV
Program uses proper and consistent naming conventions
Program uses white space to make code easier to read
Program randomly selects a question from the question bank
Program tracks the users score
Program doesn't stop till the user choses to exit
"""

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome to this Quiz Program, where you can .")
    print("\n\n(Enter in the number that corresponds with the outcome you want)")
    while True:
        choice = input("\nTake Quiz(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n")
        if choice == "1":
            take()
        elif choice == "2":
            ()
        elif choice == "3":
            ()
        elif choice == "4":
            ()
        elif choice == "5":
            ()
        elif choice == "6":
            print("\n\n\nCome Back Soon!\n\n\n")
            break
        else:
            print("\nInvalid Input (Insert an Accepted Number)")
menu()