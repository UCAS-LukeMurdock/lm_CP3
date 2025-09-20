// LM  Pokemon Battle Program

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>

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

RUBRIC:
Enumeration and Menu Implementation
Full Marks
Enumeration is correctly defined, used effectively in menu implementation, and demonstrates clear understanding in program flow
Partial Credit
Enumeration is present but with minor errors in definition or usage
No Marks
Enumeration is missing or incorrectly implemented
This criterion is linked to a Learning OutcomePokémon Structure Implementation
Full Marks
Structures for Pokémon are correctly implemented with all required properties (name, max HP, current HP, attacks, level, type)
Partial Credit
Structures are used but missing some properties or have minor implementation issues
No Marks
Structures are not used or are incorrectly implemented
This criterion is linked to a Learning OutcomeBattle System
Full Marks
Fully implemented battle system with multiple attacks, correct damage calculation, and proper turn-based flow
Partial Credit
Battle system works but lacks some features or has minor calculation errors
No Marks
Battle system is non-functional or missing
This criterion is linked to a Learning OutcomeHealing Method
Full Marks
Healing is a method available within the Pokemon structure
Partial Credit
Healing works in the program but isn't a class method
No Marks
No healing
This criterion is linked to a Learning OutcomeFinding Pokemon
Full Marks
Pokemon can be found and added to a users list of pokemon, list is checked to make sure each Pokemon is unique before it is added (Uses Operator overloading)
Partial Credit
Pokemon can be found and added to a users list of pokemon, list is checked to make sure each Pokemon is unique before it is added (no operator overloading)
No Marks
Users cannot save more than one Pokemon OR Pokemon that are not unique can be added to the players list.
This criterion is linked to a Learning OutcomeWell written code
Full Marks
Code is easy to read, uses proper data types and naming.
Partial Credit
Code is difficult to read, or not using proper industry conventions for naming and data typing
*/

// Enumeration for the menu options
enum Menu{
    Explore = 1,
    Battle,
    Heal,
    YourPokemon,
    Exit
};


struct Pokemon{
    string name;
    // string type;
    int level;
    int max_hp;
    // int current_hp;
    void heal(){ // Heals the pokemon to max HP
        cout << name << " has been healed to full health!\n";
        // current_hp = max_hp;
    }
    // vector<string> attacks;
};


// Pokemon Vectors

// Wild Pokemon vector
vector<Pokemon> wild_pokemons = {
    {"Pikachu", 5, 35},
    {"Charmander", 5, 39},
    {"Squirtle", 5, 44},
    {"Bulbasaur", 5, 45},
    {"Eevee", 5, 55},
    {"Jigglypuff", 5, 115},
    {"Meowth", 5, 40},
    {"Psyduck", 5, 50},
    {"Snorlax", 5, 160},
    {"Magikarp", 5, 20},
    {"Dragonite", 5, 91},
    {"Mewtwo", 5, 106},
    {"Gengar", 5, 60},
    {"Onix", 5, 35},
    {"Lapras", 5, 130},
    {"Vaporeon", 5, 130},
    {"Jolteon", 5, 65},
    {"Flareon", 5, 65},
    {"Articuno", 5, 90},
    {"Zapdos", 5, 90},
    {"Moltres", 5, 90}

};

// User's Pokemon vector
vector<Pokemon> user_pokemons;


// Random Number Generator
int rng(int limit){
    srand(time(0));
    int rand_num = rand() % limit;
    return rand_num;
}


void exploring(){
    int random_index = rng(wild_pokemons.size());
    Pokemon found = wild_pokemons[random_index];
    user_pokemons.push_back(found); // Adds the found pokemon to the user's pokemons vector
    cout << "You found a wild " << found.name << "!\n";
}

void battling(){
    int random_index = rng(wild_pokemons.size());
    Pokemon oponent = wild_pokemons[random_index];


    // cout << "A wild " << oponent.name << " appeared!\n";
    // cout << "You have " << user_pokemons.size() << " pokemons.\n";
    // if(user_pokemons.size()==0){
    //     cout << "You have no pokemons to battle with!\n";
    //     return;
    // }
    // cout << "Choose a pokemon to battle with:\n";
    // for(int i=0; i<user_pokemons.size(); i++){
    //     cout << "(" << i+1 << ") " << user_pokemons[i].name << " (Level " << user_pokemons[i].level << ")\n";
    // }


    // int choice;    
    // cout << "Choice: ";
    // cin >> choice;
    // cin.ignore();
    // if(choice<1 || choice>user_pokemons.size()){
    //     cout << "Invalid choice!\n";
    //     return;
    // }

    // Pokemon user_pokemon = user_pokemons[choice-1];
    // cout << "You chose " << user_pokemon.name << " (Level " << user_pokemon.level << ") to battle!\n";
    // cout << user_pokemon.name << " defeated " << oponent.name << "!\n";
    // user_pokemon.level += 1;
    // cout << user_pokemon.name << " leveled up to Level " << user_pokemon.level << "!\n";

    // user_pokemons[choice-1] = user_pokemon; // Updates the user's pokemon with the leveled up pokemon
    // wild_pokemons.erase(wild_pokemons.begin() + random_index); // Removes the oponent pokemon from the wild pokemons vector 
    
}

void healing(){
    if(user_pokemons.size()==0){
        cout << "You have no pokemons to heal!\n";
        return;
    }
    cout << "Choose a pokemon to heal:\n";
    for(int i=0; i<user_pokemons.size(); i++){
        cout << "(" << i+1 << ") " << user_pokemons[i].name << " (Level " << user_pokemons[i].level << ")\n";
    }

    int choice;    
    cout << "Choice: ";
    cin >> choice;
    cin.ignore();
    if(choice<1 || choice>user_pokemons.size()){
        cout << "Invalid choice!\n";
        return;
    }

    Pokemon user_pokemon = user_pokemons[choice-1];
    cout << user_pokemon.name << " has been healed to full health!\n";
}

void see_pokemon(){
    if(user_pokemons.size()==0){
        cout << "\nYou have no pokemon!\n";
        return;
    }
    cout << "\nYour Pokemons:\n";
    for(int i=0; i<user_pokemons.size(); i++){
        cout << i+1 << ". " << user_pokemons[i].name << " (Level " << user_pokemons[i].level << ")\n";
    }
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.

    cout << "\n\nWelcome to this Program, which...\n";
    while(true){
        int choice;

        cout <<
        "\nMenu:\n"
        "(1) Explore\n"
        "(2) Battle\n"
        "(3) Heal\n"
        "(4) Your Pokemon\n"
        "(5) Exit\n"
        "Select: ";
        cin >> choice;

        if (choice == Explore){
            exploring();
        }else if(choice == Battle){
            battling();
        }else if(choice == Heal){
            healing();
        }else if(choice == YourPokemon){
            see_pokemon();
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

//Fix healing method
//Fix battling function and attack methods
// Fix See Pokemon function
// Add Pokemon types and weaknesses/strengths

// Follow RUBRIC