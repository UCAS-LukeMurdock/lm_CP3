# LM  (Name) Project
import csv
# from file_handler import int_input

# def int_input(prompt, min = -1, max = -1): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
#     try:
#         response = int(input(prompt).strip())
#     except:
#         print("Not An Integer")
#         response = int_input(prompt,min,max)
#     if (min != -1 or max != -1) and (response < min or response > max): # If either min or max aren't -1 and the input is out of range then the user has to reinput
#         print(f"Not In Range: {min}-{max}")
#         response = int_input(prompt,min,max)
#     return response

def menu(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome, where you can see, add, remove, or search through it.")
    while True:
        choice = int_input("\nDisplay(1) Search(2) Add(3) Remove(4) Edit(5) Exit(6)\n", 1,6)
        if choice == 1:
            ()
        elif choice == 2:
            ()
        elif choice == 3:
            ()
        elif choice == 4:
            ()
        elif choice == 5:
            ()
        elif choice == 6:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
menu()
