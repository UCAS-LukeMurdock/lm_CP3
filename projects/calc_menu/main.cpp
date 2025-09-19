// LM  Calculator Menu Options Program

#include <iostream>
#include <string>
#include <memory>

using namespace std;

/*
INSTRUCTIONS:
Write a program that creates a user menu for a basic calculator using enumeration in C++. The calculator should be able to perform addition, subtraction, multiplication, and division. The program should display a menu of options, allow the user to select an operation, input two numbers, perform the calculation, and display the result. The program must continue to run till the user chooses to exit and have proper input handling. 

OUTPUT EXAMPLE: 

Calculator Menu:

Addition
Subtraction
Multiplication
Division
Exit
Enter your choice (1-5): 1 Enter first number: 10 Enter second number: 5 Result: 10 + 5 = 15

KEY REMINDERS:
Set appropriate variable types (e.g., double for temperatures).
Use at least one decimal number in your conversion calculations to ensure accurate results.
You have to get the standard library to create your inputs and outputs
Make sure your arrows are pointing the right way for the input/output stream. 
Implement error handling for invalid menu choices.

RUBRIC
Enumeration
    Enumeration is correctly defined, used effectively in menu implementation, and demonstrates clear understanding in program flow

Functional calculator menu and program flow
    Menu displays correctly, allows proper operation selection, and program runs continuously until user exits

Well Structured Code
    Code uses correct data types, inputs and output handling, error handling and organization
*/

void play(){
    cout << "Hi\n";
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this Program, which...";
    while(true){
        cout << "\nPlay Program(1)  Exit(2)\nChoice: ";
        string choice;
        cin >> choice;
        // cin.ignore();

        if(choice=="1") // Using Program
            play();
        else if(choice=="2"){ // Exiting The Program
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else
            cout << "\nIncorrect Input\n";

    }
    return 0;
}