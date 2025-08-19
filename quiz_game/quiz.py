#Luke Murdock, Quiz Handling File

from file_handler import read_file as read, intput
import random as r
import time

def choice_to_answer(choice, q):
    if choice == 1:
        return q[0]
    elif choice == 2:
        return q[1]
    elif choice == 3:
        return q[2]
    elif choice == 4:
        return q[3]

def calc_score(mean_speed, score):
    if mean_speed >= 10:
        return score
    elif mean_speed >= 8:
        return score + 1
    elif mean_speed >= 6:
        return score + 2
    elif mean_speed >= 4:
        return score + 3
    elif mean_speed >= 2:
        return score + 4
    elif mean_speed >= 0:
        return score + 5

def take(topic, file): # Lets the user take the quiz by asking questions and handling answers
    qs = read(file)
    used_qs = []
    counter = 1
    score = 0
    mean_speed = 0
    print(f"\n\nQuiz Topic: {topic}\n")

    while counter <= 10:
        if topic == "Geography" or topic == "Astronomy" or topic == "Chemistry":
            q = qs[r.randint(0,49)]
        else:
            q = qs[r.randint(0,len(qs)-1)]
            if counter -1 == len(qs):
                break
            
        if q not in used_qs:
            used_qs.append(q)
            counter += 1
            correct = q["1"]
            print(f"{counter-1}. {q.pop('Question')}") # Question
            start_time = time.time()

            # Answering
            q = list(q.values())
            r.shuffle(q)
            print(f"(1) {q[0]}\n(2) {q[1]}\n(3) {q[2]}\n(4) {q[3]}")
            choice = intput("Answer: ", 1,4)
            speed = round((time.time() - start_time), 2)

            if choice_to_answer(choice, q) == correct: # Checking
                score += 1
                print(f"\nCorrect!")
            else:
                print("\nIncorrect!")
            print(f"Speed: {speed} seconds\n")
            mean_speed += speed
            mean_speed /= 2

    print(f"\nScore: {score}/{counter-1}\nAverage Speed: {round(mean_speed, 2)} seconds\nPoints: {calc_score(mean_speed, score)}/{counter+4}\n")