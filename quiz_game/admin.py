# Luke Murdock, Admin Page
import os
from file_handler import create_file

def log_in(): # 
    password = input("\n[Forgot Password? Enter 0]\nAdmin Password: ").lower().strip()
    if password == "0":
        print("\nWho are you?")
    if password == "admin":
        print("\nAs admin you can make quizzes composed of question sets (The question and four answers).")
        q_sets = []

        while True:
            q_set = {}
            q = input("\n[Enter 0 to finish creating quiz]\n[Enter 1 to give up creating this quiz]\nWhat question do you have?:\n")
            if q == "0":
                break
            if q == "1":
                return

            correct_a = input("What is the correct answer?:\n")
            a2 = input("What is an incorrect answer?:\n")
            a3 = input("What is another incorrect answer?:\n")
            a4 = input("What is your last incorrect answer?:\n")

            q_set["Question"] = q
            q_set["1"] = correct_a
            q_set["2"] = a2
            q_set["3"] = a3
            q_set["4"] = a4

            q_sets.append(q_set)

        # Create new file with q_sets and with relative path saved somewhere
        print(q_sets)

        file_name = f"{input("\nWhat is your quiz's name?:\n").strip().replace(" ", "_")}.csv"
        print(create_file(file_name, q_sets))
            

def admin_quizzes(): # 

    # Get the list of all files and directories
    path = "C:/Users/luke.murdock/Documents/lm_CP3/quiz_game"
    files = os.listdir(path)
    print("Files and directories in '", path, "' :")
    # prints all files
    print(files)

    wrong_files = ['admin.py', 'admin_qs.csv', 'astronomy.csv', 'chemistry.csv', 'file_handler.py', 'geography.csv', 'main.py', 'pseudocode.txt', 'quiz.py', '__pycache__']
    for wrong_file in wrong_files:

        files.remove("")
    # ['admin.py', 'admin_qs.csv', 'astronomy.csv', 'chemistry.csv', 'file_handler.py', 'geography.csv', 'main.py', 'pseudocode.txt', 'quiz.py', '__pycache__']

    # Fix this list and removing and fix where new files go