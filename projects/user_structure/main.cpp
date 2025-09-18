// LM  User Structure Program

#include <iostream>
#include <string>
#include <vector>

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

bool operator==(const User& first, const User& second){
    return (first.name == second.name &&
        first.password == second.password &&
        first.isAdmin == second.isAdmin
    );
}

ostream& operator<<(ostream& stream, User& print_user){
    stream << print_user.name;
    return stream;
}

// Users vector
vector<User> users;

void add_users(){ // Adds the 10 prexisting users to the 'users' vector
    users.push_back({"Admin Luke", "0", true});
    users.push_back({"Nick", "1", true});
    users.push_back({"Ms.LaRose", "2", true});
    users.push_back({"Matt", "3", false});
    users.push_back({"David", "4", false});
    users.push_back({"Turtle", "5", false});
    users.push_back({"Cat", "6", false});
    users.push_back({"Jacob", "7", false});
    users.push_back({"Jake", "8", false});
    users.push_back({"Jack", "9", false});
}

// Functions
void compare(User new_user){ // Compares the new user with the existing users
    for(auto user: users){
        if(user == new_user){
            cout << "\nUser '" << new_user << "' already exists\n";
            return;
        }
    }
    cout << "\n\nWelcome, User '" << new_user << "'\n";
}

User input(){ // Lets you input a user and their details
    string user_name;
    string user_password;
    string admin_input;
    bool is_user_admin;

    cout << "\nInput your name: ";
    getline(cin, user_name);

    cout << "\nInput your password: ";
    getline(cin, user_password);

    cout << "\n(Input 'True' if you are an admin)\nInput your admin_status: ";
    getline(cin, admin_input);
    is_user_admin = (admin_input == "True" || admin_input == "true");

    User new_user = {user_name, user_password, is_user_admin};
    return new_user;
}

int main(){ // This welcomes the user and lets the user choose to use or exit the program.

    add_users();

    cout << "\n\nWelcome to this User Program, which stores user information and will take in new users.";
    while(true){
        cout << "\nInput User Info(1)  Exit(2)\nChoice: ";
        string choice;
        getline(cin, choice);

        if(choice=="1") // Using Program
            compare(input());
        else if(choice=="2"){ // Exiting The Program
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else
            cout << "\nIncorrect Input\n";
    }
    return 0;
}

