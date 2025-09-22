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

// Enumeration for the menu options
enum Menu{ 
    Addition = 1,
    Subtraction,
    Multiplication,
    Division,
    Exit
};


// Checks if the input is valid (It needs to be a number)
bool check_input(){ 
    if(cin.fail()){
        cin.clear(); // clear error state
        cin.ignore(1, '\n'); // discard invalid input
        cout << "\n\nInvalid Input Type\n";
        return false;
    }
    return true;
}

// Asks the user for two numbers and returns them
bool ask_nums(float& num1, float& num2){ 
    cout << "\nEnter first number: ";
    cin >> num1;
    if (check_input() == false) {
        return false;
    }
    cout << "\nEnter second number: ";
    cin >> num2;
    if (check_input() == false) {
        return false;
    }
    return true;
}

// Calculator Functions
float add(float num1, float num2){
    return num1 + num2;
}
float subtract(float num1, float num2){
    return num1 - num2;
}
float multiply(float num1, float num2){
    return num1 * num2;
}
float divide(float num1, float num2){
    return num1 / num2;
}


int main(){ // This welcomes the user and prints the result to an inputted, simple equation or they can exit the program.
    cout << "\n\nWelcome to this Calculator Program, which lets you choose an operation and input two numbers for it to performed on.\n";
    while(true){

        int choice;

        cout <<
        "\n\nNew Calculation:\n"
        "\nWhich Operation?\n"
        "(1) Addition\n"
        "(2) Subtraction\n"
        "(3) Multiplication\n"
        "(4) Division\n"
        "(5) Exit\n"
        "Select: ";

        cin >> choice;
        if(check_input() == false)
            continue;
        
        float num1, num2;

        if (choice == Addition){
            if (ask_nums(num1, num2) == true)
                cout << "\n\nResult: " << num1 << " + " << num2 << " = " << add(num1, num2) << endl;
        }else if(choice == Subtraction){
            if (ask_nums(num1, num2) == true)
                cout << "\n\nResult: " << num1 << " - " << num2 << " = " << subtract(num1, num2) << endl;
        }else if(choice == Multiplication){
            if (ask_nums(num1, num2) == true)
                cout << "\n\nResult: " << num1 << " * " << num2 << " = " << multiply(num1, num2) << endl; 
        }else if(choice == Division){

            if (ask_nums(num1, num2) == true)
                if(num2 == 0){
                    cout << "\nDivide by Zero Error\n";
                }else{
                    cout << "\n\nResult: " << num1 << " / " << num2 << " = " << divide(num1, num2) << endl;
                }
                
        }else if(choice == Exit){
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else{
            cout << "\n\nInvalid Input\n";
        }
    }
    return 0;
}