// LM  User Structure Program

#include <iostream>
#include <string>
// #include <memory>

using namespace std;

/*
Write a program that takes in a username, password, and admin status (you can do more but that is the minimum). The program then uses that information to create a user object from a structure. 
It then needs to compare that user with a list of already existing users (10 users minimum) to see if the user already exists.

OUTPUT EXAMPLE: 
User: Alex LaRose
Already exists. 
OR
Welcome
User: Alex LaRose

Correctly takes input for username, password, and admin status Creates a user object from a structure using the input Compares the new user with existing users and provides appropriate output
Properly defines a user structure with at least username, password, and admin status Correctly initializes user objects using the structure
Creates a list of at least 10 existing users
Correctly overloads an operator (e.g., ==) to compare user objects Properly implements the comparison logic in the overloaded operator
Correctly includes and uses the standard library for input/output operations Uses the correct arrow directions for input/output streams
Properly declares and uses appropriate variable types throughout the program
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

