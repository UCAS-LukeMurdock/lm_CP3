// LM  Program

#include <iostream>
#include <string>
// #include <memory>

using namespace std;

// Enumeration for the menu options
enum Menu{
    First = 1,
    Second,
    Third,
    Fourth,
    Exit
};


void play(){
    cout << "Hi\n";
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this Program, which...\n";
    while(true){
        int choice;

        cout <<
        "\nMenu:\n"
        "(1) First\n"
        "(2) Second\n"
        "(3) Third\n"
        "(4) Fourth\n"
        "(5) Exit\n"
        "Select: ";
        cin >> choice;

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
        }else{ // Any Invalid input
            
            // In case of non-integer input
            cin.clear(); // clear error state
            cin.ignore(10000, '\n'); // discard invalid input

            cout << "\nInvalid Input\n";;
        }
    }
    return 0;
}




// LM  {} Notes

#include <iostream>
// #include <string>
// #include <memory>

using namespace std;


void play(){
    cout << "\n";
}


int main(){

    cout << "\n";

    return 0;
}


// NOTES QUESTIONS
