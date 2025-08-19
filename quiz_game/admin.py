# Luke Murdock, Admin Page
from file_handler import create_file, get_quizzes, intput
from quiz import take

def log_in(): # 
    password = input("\n[Forgot Password? Enter 0]\nAdmin Password: ").lower().strip()
    if password == "0":
        print("\nWho are you?")
    if password == "admin":
        print("\nAs admin you can make quizzes composed of question sets (The question and four answers).")
        q_sets = []

        while True:
            q = input("\n[Enter 0 to finish creating quiz]\n[Enter 1 to give up creating this quiz]\nWhat question do you have?:\n")
            if q == "0":
                break
            if q == "1":
                return

            correct_a = input("What is the correct answer?:\n")
            a2 = input("What is an incorrect answer?:\n")
            a3 = input("What is another incorrect answer?:\n")
            a4 = input("What is your last incorrect answer?:\n")

            q_set = {
                "Question": q,
                "1": correct_a,
                "2": a2,
                "3": a3,
                "4": a4
            }

            q_sets.append(q_set)

        # Create new file with q_sets and with relative path saved somewhere
        print(q_sets)

        file_name = f"{input("\nWhat is your quiz's name?:\n").lower().strip().replace(" ", "_")}.csv"
        print(create_file(file_name, q_sets))
            

def quiz_name_format(quiz):
    return quiz[:-4].title().replace("_", " ")


def admin_quizzes(): # 

    quizzes = get_quizzes()
    while True:

        print("\nWhich custom quiz do you want to take?\n(0) Exit")
        for index, quiz in enumerate(quizzes):
            print(f"({index+1}) {quiz_name_format(quiz)} Quiz") # Make the quiz name look normal?

        choice = intput("Choice: ", 0,len(quizzes))
        if choice == 0:
            break

        choice = quizzes[choice -1]
        take(quiz_name_format(choice), f"quiz_game/{choice}")