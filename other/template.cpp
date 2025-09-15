// LM  Program

#include <iostream>
// #include <string>
// #include <memory>

using namespace std;


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
