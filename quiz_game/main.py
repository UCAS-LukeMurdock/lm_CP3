# Luke Murdock, Quiz Game
from file_handler import intput
from quiz import take
from admin import log_in, admin_quizzes

# Admin Password is 'admin'

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome to this Quiz Program, where you can either take a geogrpahy quiz, astronomy quiz, chemistry quiz, or one made by the admin.\nEach topic gives you at most 10 questions and you get points on accuracy and speed.")
    print("\n\n(Enter in the number that corresponds with the outcome you want)")

    while True:
        print("\nWhat do you want to do?\n(1) Geography Quiz\n(2) Astronomy Quiz\n(3) Chemistry Quiz\n(4) Pick an Admin Quiz\n(5) Admin Log In\n(6) Exit")
        choice = intput("Choice: ", 1,6)

        if choice == 1:
            take("Geography", "quiz_game/geography.csv")
        elif choice == 2:
            take("Astronomy", "quiz_game/astronomy.csv")
        elif choice == 3:
            take("Chemistry", "quiz_game/chemistry.csv")
        elif choice == 4:
            admin_quizzes()
        elif choice == 5:
            log_in()
        elif choice == 6:
            print("\n\nCome Back Soon!\n\n")
            break
        else:
            print("Something Broke")
menu()