#  Reuses


def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome, where you can see, add, remove, or search through it.")
    while True:
        choice = input("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n")
        if choice == "1":
            ()
        elif choice == "2":
            ()
        elif choice == "3":
            ()
        elif choice == "4":
            ()
        elif choice == "5":
            ()
        elif choice == "6":
            print("\n\n\nCome Back Soon!\n\n\n")
            break
        else:
            print("\nInvalid Input (Enter a number 1-6)")
menu()



# else:
#     print("Incorrect Input, Either Not an Integer or Out of Range, Try Again")
        #Oops no looping

def intput(prompt, min = -1, max = -1): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
    try:
        response = int(input(prompt).strip())
    except:
        print("Not An Integer")
        response = intput(prompt,min,max)
    if (min != -1 or max != -1) and (response < min or response > max): # If either min or max aren't -1 and the input is out of range then the user has to reinput
        print(f"Not In Range: {min}-{max}")
        response = intput(prompt,min,max)
    return response
    
def int_input(prompt, max = 0, min = 0, need_range = True): # Checks and solves errors in integer inputs (Has Range If Needed)
    while True:
        try: 
            response = int(input(prompt).strip())
        except:
            print("Not An Integer")
            continue
        if need_range == True and response < min and response > max:
            break
        else:
            print("Not In Range")
            continue
    return response

def num_input(prompt, range = 0, data_type = "int"): # Checks and solves errors in int and float inputs (Has Range If Needed)
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt).strip())
            elif data_type == "float":
                response = float(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

#inputs

def int_input(text): # Only takes in integers
    while True:
        try: output = int(input(text))
        except ValueError:
            print("Invalid Input! (only integers accepted)")
            input("Press enter to try again")
            continue
        return output
def str_input(text): # Only takes in strings
    while True:
        try: output = str(input(text))
        except ValueError:
            print("String Input! (only strings accepted)")
            input("Press enter to try again")
            continue
        return output
def float_input(text): # Only takes in floats
    while True:
        try: output = float(input(text))
        except ValueError:
            print("Invalid Input! (only floats accepted)")
            input("Press enter to try again")
            continue
        return output
def cs(): # Clear Screen
    print("\033c",end="")

'''
tasks = []
# 
with open("To Do List/list.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        task = {}
        for detail_index, detail in enumerate(row):
            task.update({detail_types[detail_index]:row[detail_index]})
        tasks.append(task)

def write(): # 
    with open ("To Do List/list.csv", "w", newline="") as file:
        fieldnames = ["Name", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)


        

with open("Movie Recommender/Movies list.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        movie = {}
        for detail_index, detail in enumerate(row):
            movie.update({detail_types[detail_index]:row[detail_index]})
        movies.append(movie)
'''