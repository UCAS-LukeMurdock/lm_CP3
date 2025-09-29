// LM  Program

#include <iostream>
#include <string>

using namespace std;

/*

*/

// Enumeration for the menu options
enum Menu{
    First = 1,
    Second,
    Third,
    Fourth,
    Exit
};


float num_input(){ // Checks if the input is valid (It needs to be a number [float])
    float input;
    while (!(cin >> input)){
        cin.clear(); // clear error state
        cin.ignore(10000, '\n'); // discard invalid input completely
        cout << "\nInvalid Input Type (Enter in a Number)\nNew Input: ";
    }
    return input;
}


void play(){
    cout << "Hi\n";
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this Program, which...\n";
    while(true){
        float choice;

        cout <<
        "\nMenu:\n"
        "(1) First\n"
        "(2) Second\n"
        "(3) Third\n"
        "(4) Fourth\n"
        "(5) Exit\n"
        "Choice: ";

        choice = num_input();

        if (choice == First){
            cout << "\nFirst option\n";
        }else if(choice == Second){
            cout << "\nSecond option\n";
        }else if(choice == Third){
            cout << "\nThird option\n";
        }else if(choice == Fourth){
            cout << "\nFourth option\n";
        }else if(choice == Exit){
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else{
            cout << "\nInvalid Input (Enter an Integer 1-5)\n";;
        }
    }
    return 0;
}