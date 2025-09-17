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

struct User {
    string name;
    string password;
    bool isAdmin;
};

// Overloading

User existing_users[10] = {};

void make_user_list(){
    User luke;
    luke.name = "Admin Luke";
    luke.password = "0";
    luke.isAdmin = true;

    User nick;
    nick.name = "Nick";
    nick.password = "1";
    nick.isAdmin = true;

    User luke;
    luke.name = "";
    luke.password = "2";
    luke.isAdmin = true;

    User luke;
    luke.name = "";
    luke.password = "3";
    luke.isAdmin = false;

    User luke;
    luke.name = "";
    luke.password = "4";
    luke.isAdmin = false;

    User luke;
    luke.name = "";
    luke.password = "5";
    luke.isAdmin = false;

    User luke;
    luke.name = "";
    luke.password = "6";
    luke.isAdmin = false;

    User luke;
    luke.name = "";
    luke.password = "7";
    luke.isAdmin = false;

    User luke;
    luke.name = "";
    luke.password = "8";
    luke.isAdmin = false;

    User luke;
    luke.name = "";
    luke.password = "9";
    luke.isAdmin = false;
}

void input(){ // Lets you input
    string user_name;
    string user_password;
    bool isUserAdmin;
    cout << "Input your name, password, ";
    cin >> user_name, user_password, isUserAdmin;
    cout << "\n";
}

void compare

int main(){ // This welcomes the user and lets the user choose to use or exit the program.

    User luke;
    luke.name = "";
    luke.password = "";
    luke.isAdmin = true;
    User luke;
    luke.name = "";
    luke.password = "";
    luke.isAdmin = true;
    User luke;
    luke.name = "";
    luke.password = "";
    luke.isAdmin = true;
    User luke;
    luke.name = "";
    luke.password = "";
    luke.isAdmin = true;
    User luke;
    luke.name = "";
    luke.password = "";
    luke.isAdmin = true;User luke;
    luke.name = "";
    luke.password = "";
    luke.isAdmin = true;


    cout << "\n\nWelcome to this User Program, which stores user information and will take in new users.";
    while(true){
        cout << "\nInput User Info(1)  Exit(2)\nChoice: ";
        string choice;
        cin >> choice;
        cin.ignore();

        if(choice=="1") // Using Program
            input();
        else if(choice=="2"){ // Exiting The Program
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else
            cout << "\nIncorrect Input\n";

    }
    return 0;
}

