# Luke Murdock, Read & Write to Files, Integer Input Handler, and other Handlers
import csv

def read_file(): # Turns a file into a list of dictionaries
    dicts = []
    with open("quiz_game/question.csv", "r") as file:
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

def write_file(dicts): # Writes the list of dictonary onto the file
    with open ("quiz_game/question.csv", "w", newline="") as file:
        fieldnames = ["",""]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dicts)