#Luke Murdock, Quiz Handling File

from file_handler import read_file as read, intput
import random as r
import time

def take(topic, file): # Lets the user take the quiz by asking questions and handling answers
    qs = read(file)
    used_qs = []
    counter = 1
    score = 0
    mean_speed = 0
    print(f"\n\nQuiz Topic: {topic}\n")

    while counter <= 10:
        if topic == "Admin's Questions":
            q = qs[r.randint(0,len(qs)-1)]
        else:
            q = qs[r.randint(0,49)]
            
        if q not in used_qs:

            used_qs.append(q)
            counter += 1
            correct = q["1"]

            print(f"{counter-1}. {q.pop('Question')}")
            start_time = time.time()
            q = list(q.values())
            r.shuffle(q)

            print(f"(1) {q[0]}\n(2) {q[1]}\n(3) {q[2]}\n(4) {q[3]}")
            choice = intput("Answer: ", 1,4)
            speed = round((time.time() - start_time), 2)
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
                print(f"\nCorrect!")
            else:
                print("\nIncorrect!")
            print(f"Speed: {speed} seconds\n")
            mean_speed += speed
            mean_speed /= 2

    if mean_speed >= 10:
        points = score
    elif mean_speed >= 8:
        points = score + 1
    elif mean_speed >= 6:
        points = score + 2
    elif mean_speed >= 4:
        points = score + 3
    elif mean_speed >= 2:
        points = score + 4
    elif mean_speed >= 0:
        points = score + 5

    print(f"\nScore: {score}/10\nAverage Speed: {round(mean_speed, 2)} seconds\nPoints: {points}/15\n")