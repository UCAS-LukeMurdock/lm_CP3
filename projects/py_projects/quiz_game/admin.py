# Luke Murdock, Admin Page
from file_handler import create_file, get_quizzes, intput
from quiz import take

def log_in(): # Lets the user log in as admin and create a quiz
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

        if q_sets == []:
            print("\nThe quiz doesn't have any questions so it can't be created.\n")
            return

        for q_set in q_sets:
            print(f"{q_set["Question"]}: {q_set["1"]} (Correct), {q_set["2"]}, {q_set["3"]}, {q_set["4"]}")

        file_name = f"{input("\n[Enter 0 to Exit]\nWhat is your quiz's name?:\n").lower().strip().replace(" ", "_")}.csv"
        if file_name == "0.csv":
            return
        print(create_file(file_name, q_sets))



def quiz_name_format(quiz): # Formats a file name into a more readable format
    return quiz[:-4].title().replace("_", " ")


def admin_quizzes(): # Gets the custom quizzes and lets the user take them

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