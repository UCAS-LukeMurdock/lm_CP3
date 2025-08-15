#Luke Murdock, Quiz Handling File

from file_handler import write_file as write, read_file as read, intput
import random as r

def take(topic, file): # Lets the user take the quiz by asking questions and handling answers
    qs = read(file)
    used_qs = []
    counter = 1
    score = 0
    print(f"\n\nQuiz Topic: {topic}\n")

    while counter <= 10:
        if topic != "Admin's Questions":
            q = qs[r.randint(0,49)]
        else:
            q = qs[r.randint(0,len(qs)-1)]
        if q not in used_qs:

            used_qs.append(q)
            counter += 1
            correct = q["1"]

            print(q.pop("Question"))
            q = list(q.values())
            r.shuffle(q)

            print(f"(1) {q[0]}\n(2) {q[1]}\n(3) {q[2]}\n(4) {q[3]}")
            choice = intput("Answer: ", 1,4)
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
                print("Correct!\n")
            else:
                print("Incorrect!\n")

    print(f"Score: {score}/10")
                
