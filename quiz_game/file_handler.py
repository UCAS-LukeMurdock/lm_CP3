# Luke Murdock, Read & Write to Files, Integer Input Handler, and other Handlers
import csv
import os

def read_file(file_path): # Turns a file into a list of dictionaries
    dicts = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)

        for row_index, row in enumerate(reader):
            if row_index == 0:
                detail_types = row
                continue

            dict = {}
            for detail_index, detail in enumerate(row):
                dict.update({detail_types[detail_index]:detail})
            dicts.append(dict)
            
    return dicts


def create_file(file_name, data): # Lets the admin create a new csv file that holds their created quiz

        # Define the target folder and filename
    folder_path = "quiz_game"
    full_path = os.path.join(folder_path, file_name)

    # Ensure the directory exists
    # os.makedirs(folder_path, exist_ok=True) # exist_ok=True prevents error if folder already exists

    try:
        with open(full_path, 'x', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Question', '1', '2', '3', '4'])
            writer.writeheader()
            writer.writerows(data)
        return (f"\nQuiz '{file_name[:-4].title().replace("_", " ")}' created successfully.")
    except FileExistsError:
        return (f"\nError: Quiz '{file_name[:-4].title().replace("_", " ")}' already exists.")
    except Exception as e:
        return (f"\nAn error occurred: {e}")


def get_quizzes(): # Get the list of all files in the folder and returns the custom ones
    path = "quiz_game"
    files = os.listdir(path)

    wrong_files = ['admin.py', 'astronomy.csv', 'chemistry.csv', 'file_handler.py', 'geography.csv', 'main.py', 'pseudocode.txt', 'quiz.py', '__pycache__']
    for wrong_file in wrong_files:
        files.remove(wrong_file)

    return files



def intput(prompt, min = -1, max = -1): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
    try:
        response = int(input(prompt).strip())
    except:
        print("\nNot An Integer\n")
        response = intput(prompt,min,max)
    if (min != -1 or max != -1) and (response < min or response > max): # If either min or max aren't -1 and the input is out of range then the user has to reinput
        print(f"\nNot In Range: {min}-{max}\n")
        response = intput(prompt,min,max)
    return response
