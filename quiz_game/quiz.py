#Luke Murdock, Quiz Handling File

from file_handler import write_file as write, read_file as read, intput
import random as r

def take(): # Lets the user take the quiz by asking questions and handling answers
    qs = read()
    used_qs = []
    counter = 1
    score = 0
    print("\n\nQuiz Topic: Geography")

    while counter <= 10:
        q = qs[r.randint(0,49)]
        if q not in used_qs:

            counter += 1
            correct = q["1"]
            print(q.pop("Question"))
            # r.shuffle(q)
            q = list(q.values())

            choice = intput(f"{q[0]}(1)\n{q[1]}(2)\n{q[2]}(3)\n{q[3]}(4)\nAnswer: ", 1,4)
            if choice == 1:
                answer = q[0]
            elif choice == 2:
                answer = q[1]
            elif choice == 3:
                answer = q[2]
            elif choice == 4:
                answer = q[3]
                
            if answer == correct:
                score += 1
                print("Correct!")
            else:
                print("Incorrect!")

    print(f"Score: {score}/10")
                
