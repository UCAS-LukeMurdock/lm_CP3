// LM  Pokemon Battle Program

#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
INSTRUCTIONS:
Write a program that creates a Pokémon battle game using structures for Pokémon and enumeration for the menu in C++. The game should allow users to explore (find Pokémon), battle, heal Pokémon, and exit the game. Implement structures for Pokémon that include names, max HP, attacks, and level. Use enumeration for the main menu options.

The game must include the following features:

A main menu with options to explore, battle, heal, and exit.
Exploration feature to find and catch Pokémon.
Battle system where users can fight against wild Pokémon or other trainers.
Healing option to restore Pokémon HP.
Multiple attack options for each Pokémon during battles.
Different Pokémon types with associated weaknesses and strengths.
Type-based damage bonuses during battles.

OUTPUT EXAMPLE:

Pokémon Battle Game Menu:

Explore
Battle
Heal Pokémon
Exit
Enter your choice (1-4): 1

You found a wild Pikachu! Do you want to catch it? (Y/N): Y

Pikachu has been added to your team!

KEY REMINDERS:
Use structures to define Pokémon with properties like name, max HP, current HP, attacks, level, and type.
Implement enumeration for the main menu options.
Create multiple attack options for each Pokémon.
Implement a type system with weaknesses and strengths (e.g., Water is strong against Fire).
Use appropriate variable types and error handling.
Ensure the game continues running until the user chooses to exit.
Implement proper input validation and error handling.

BONUS (Rubber Duck Prize):
To earn a rubber duck prize, include multiple attack options that users can select during battle, and implement a comprehensive type system with proper weaknesses and strengths that provide damage bonuses.
*/

struct {
    string name;
    // string type;
    int level;
    int max_hp;
    // int current_hp;
    // vector<string> attacks;
};

// Pokemon vector

void explore(){
    cout << "Hi\n";
}

void battle(){
    cout << "Hi\n";
}

void heal(){
    cout << "Hi\n";
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this Program, which...";
    while(true){
        cout << "\nMenu:\n(1) Explore\n(2) Battle\n(3) Heal Pokemon\n(4) Exit\nChoice: ";
        string choice;
        cin >> choice;
        // cin.ignore();

        if(choice=="1")
            explore();
        else if(choice=="2")
            battle();
        else if(choice=="3")
            heal();
        else if(choice=="4"){ // Exiting The Program
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else
            cout << "\nIncorrect Input\n";

    }
    return 0;
}