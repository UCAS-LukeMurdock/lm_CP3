# Luke Murdock, Quiz Game
from file_handler import intput
from quiz import take
from admin import log_in

"""
Create a quiz game that asks the user at least 10 questions (randomly selected from a csv that holds at least 50 questions [yes you can use AI to create your questions and answers]).
Let users answer (they should be multiple choice questions but make sure your user knows what to do to select their choice)
Tell the user if they got the question right or wrong
Give the overall score at the end
The program needs to run until the user selects to quit

MORE CHALLENGES:
Create a user interface with tkinter or turtle that lets users click on the answers they want (5 points)
|Allow users to select from different lists of questions (2 points)
|Allow users to create lists of questions (2 points)
|User profiles (Admin users can create new lists of questions, normal users can just select from lists of questions to do) (4 points)
Give different point amounts based on how quickly they answer (5 points)
||Shuffle the order the answers are displayed (1 point)

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
    print("\n\nWelcome to this Quiz Program, where you can either take a geogrpahy quiz, astronomy quiz, chemistry quiz, or one made by the admin.")
    print("\n\n(Enter in the number that corresponds with the outcome you want)")

    while True:
        print("\nWhat do you want to do?\n(1) Geography Quiz\n(2) Astronomy Quiz\n(3) Chemistry Quiz\n(4) Admin Quiz\n(5) Admin Log In\n(6) Exit")
        choice = intput("Choice: ", 1,6)
        if choice == 1:
            take("Geography", "quiz_game/geography.csv")
        elif choice == 2:
            take("Astronomy", "quiz_game/astronomy.csv")
        elif choice == 3:
            take("Chemistry", "quiz_game/chemistry.csv")
        elif choice == 4:
            take("Admin's Questions", "quiz_game/admin_qs.csv")
        elif choice == 5:
            log_in()
        elif choice == 6:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
menu()