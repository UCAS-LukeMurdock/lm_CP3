// LM  Dynamic Array

#include <iostream>
#include <string>
#include <memory>

using namespace std;


void enter_colors(){ // This lets the user enter colors and it prints them out at the end
    int capacity = 5;
    shared_ptr <string[]> inputs(new string[capacity]); // Makes a shared pointer of a string array
    int entries = 0;

    cout << "\n[Enter 0 to Stop]" << endl;
    while(true){ // Loop that lets you continually enter colors into the array
        cout << "Enter a Color: ";
        string input;
        getline(cin, input);
        if(input == "0")
            break;

        inputs[entries] = input;
        if(cin.fail()) break;
        entries++;


        if(entries == capacity){ // Makes array dynamic
            capacity += 5;
            shared_ptr <string[]> temp(new string[capacity]);

            for(int i = 0; i < entries; i++)
                temp[i] = inputs[i];

            inputs.reset();
            inputs = temp;
        }
    }
    cout << "\nEntered Colors: ";
    for (int i=0; i < entries; i++) // Prints out the colors in the array
        cout << inputs[i] << ", ";
    cout << endl;
}


int main(){ // This welcomes the user and lets the user choose to use the program or exit.

    cout << "\n\nWelcome to this List of Colors Program, where you can enter in as many colors as you want.";
    while(true){
        cout << "\nPlay(1)  Exit(2)\nChoice: ";
        string choice;
        cin >> choice;
        cin.ignore();

        if(choice=="1") // Using Program
            enter_colors();
        else{
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }
    }
    return 0;
}