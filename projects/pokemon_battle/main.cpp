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

// ENUMERATIONS
enum Menu{ // Enumeration for the main menu options
    Explore = 1,
    Battle,
    Heal,
    YourPokemon,
    Exit
};

enum Action{ // Enumeration for the action options in battle
    Attack = 1,
    SpecialAttack,
    StatusMove,
    Run
};


// POKEMON STRUCTURE
struct Pokemon{
    string name;
    string type;
    int level;
    int max_hp;
    int current_hp;
    int atk_power;
    string atk_name;
    string special_atk_name;
    string status_move_name;

    void display_info(){ // Displays all the pokemon's information
        cout << "Name: " << name << endl;
        cout << "Type: " << type << endl;
        cout << "Level: " << level << endl;
        cout << "HP: " << current_hp << "/" << max_hp << endl;
        cout << "Attack Power: " << atk_power << endl;
        cout << "Attack: " << atk_name << endl;
        cout << "Special Attack: " << special_atk_name << endl;
        cout << "Status Move: " << status_move_name << endl;
    }

    void heal(){ // Heals the pokemon to max HP
        current_hp = max_hp;
        cout << name << " has been healed to full health!\n";
    }

    void level_up(bool is_opponent = false){ // Increases the pokemon's level by 1
        level += 1;
        max_hp += 5; // Increase max HP by 5 for each level up
        atk_power += 2; // Increase attack power by 2 for each level up
        if (is_opponent == true){
            current_hp = max_hp; // If opponent, heal to full
        }else{
            current_hp += 5;
            cout << name << " leveled up from Level " << (level -1) << " to Level " << level << "!\n";
            
        }
    }

    void action(Pokemon& target, string action_name){ // Attacks the target pokemon with the selected attack
        int damage = 0;
        cout << name << " used " << action_name << " on " << target.name << "!\n";
        
        if (action_name == atk_name) {
            damage = atk_power;
        } else if (action_name == special_atk_name) {
            damage = atk_power * 2; // Special attack does double damage
            current_hp -= atk_power / 2; // Recoil damage to self
            if(current_hp < 0) 
                current_hp = 0;
            cout << name << " took " << atk_power /2 << " recoil damage!\n";
        } else if (action_name == status_move_name) {
            target.atk_power -= 4 + level/2; // Status move decreases target's attack power
            if (target.atk_power < 1){
                target.atk_power = 1; // Minimum attack power is 1
                cout << target.name << " is as weak as it can be!\n\n";
            }else 
                cout << target.name << " is now weakened and will do less damage!\n\n";
            return; // No damage dealt
        }
        target.current_hp -= damage;
        if(target.current_hp < 0) 
            target.current_hp = 0;
        cout << target.name << " took " << damage << " damage!\n";
    }
};

// OVERLOADING

 // Overloads the == operator to compare two pokemons by name
bool operator== (const Pokemon& pokemon1, const Pokemon& pokemon2){
    return pokemon1.name == pokemon2.name;
}

// Overloads the << operator to print a pokemon's name
ostream& operator<<(ostream& stream, Pokemon& pokemon){
    stream << pokemon.name;
    return stream;
}


// POKEMON VECTORS

// Wild Pokemon vector       Types: Normal, Fire, Water, Electric, Grass
vector<Pokemon> wild_pokemons = {
    // name, type, level, max_hp, current_hp, atk_power, atk_name, special_atk_name, status_move_name

    // Electric Type
    {"Pikachu", "Electric", 1, 35, 35, 10, "Thunder Shock", "Thunderbolt", "Tail Whip"},
    {"Magnemite", "Electric", 1, 25, 25, 11, "Thunder Shock", "Thunderbolt", "Flash"},
    {"Voltorb", "Electric", 1, 40, 40, 12, "Tackle", "Spark", "Self-Destruct"},

    // Fire Type
    {"Growlithe", "Fire", 1, 55, 55, 14, "Bite", "Flamethrower", "Roar"},
    {"Charmander", "Fire", 1, 39, 39, 12, "Ember", "Flamethrower", "Smokescreen"},
    {"Vulpix", "Fire", 1, 38, 38, 12, "Ember", "Flamethrower", "Will-O-Wisp"},
    {"Ponyta", "Fire", 1, 50, 50, 13, "Tackle", "Flame Wheel", "Agility"},

    // Water Type
    {"Lapras", "Water", 1, 130, 130, 16, "Water Gun", "Ice Beam", "Sing"},
    {"Psyduck", "Water", 1, 50, 50, 11, "Water Gun", "Confusion", "Disable"},
    {"Squirtle", "Water", 1, 44, 44, 11, "Water Gun", "Hydro Pump", "Bubble"},
    {"Poliwag", "Water", 1, 40, 40, 10, "Bubble", "Hydro Pump", "Hypnosis"},
    {"Seel", "Water", 1, 65, 65, 10, "Headbutt", "Aqua Jet", "Rest"},
    {"Krabby", "Water", 1, 30, 30, 11, "Bubble Beam", "Crabhammer", "Leer"},
    {"Shellder", "Water", 1, 30, 30, 11, "Tackle", "Icicle Spear", "Withdraw"},
    {"Magikarp", "Water", 1, 20, 20, 5, "Splash", "Tackle", "Flail"},

    // Grass Type
    {"Exeggcute", "Grass", 1, 60, 60, 10, "Confusion", "Solar Beam", "Leech Seed"},
    {"Bulbasaur", "Grass", 1, 45, 45, 9, "Vine Whip", "Solar Beam", "Leech Seed"},
    {"Oddish", "Grass", 1, 45, 45, 9, "Absorb", "Solar Beam", "Poison Powder"},
    {"Bellsprout", "Grass", 1, 50, 50, 10, "Vine Whip", "Razor Leaf", "Sleep Powder"},

    // Normal Type
    {"Snorlax", "Normal", 1, 160, 160, 15, "Body Slam", "Hyper Beam", "Rest"},
    {"Eevee", "Normal", 1, 55, 55, 10, "Tackle", "Swift", "Sand Attack"},
    {"Meowth", "Normal", 1, 40, 40, 10, "Scratch", "Bite", "Fake Out"},
    {"Rattata", "Normal", 1, 30, 30, 10, "Tackle", "Hyper Fang", "Quick Attack"},
    {"Jigglypuff", "Normal", 1, 115, 115, 8, "Pound", "Double Slap", "Sing"},
    {"Pidgey", "Normal", 1, 40, 40, 10, "Tackle", "Wing Attack", "Sand Attack"},
    {"Zubat", "Normal", 1, 40, 40, 10, "Bite", "Air Cutter", "Confuse Ray"}
};

// User's Pokemon vector
vector<Pokemon> user_pokemons;


// UTILITY FUNCTIONS
// Random Number Generator
int rng(int limit){
    srand(time(0));
    int rand_num = rand() % limit;
    return rand_num;
}

// Checks if a number input is valid (It needs to be a number [float])
float num_input(){ 
    float input;
    while (!(cin >> input)){
        cin.clear(); // clear error state
        cin.ignore(10000, '\n'); // discard invalid input completely
        cout << "\nInvalid Input Type (Enter in a Number)\nNew Input: ";
    }
    return input;
}


// Checks inputs to make sure they don't fail
void check_input(){
    if(cin.fail()){
        cin.clear(); // clear error state
        cin.ignore(10000, '\n'); // discard invalid input completely
    }
}

// Catching function to catch a found or battled pokemon
void catching(Pokemon found, bool battled = false){
    cout << "Do you want to try and catch the " << found << "? (Y/N): ";
    string choice;
    cin >> choice;
    check_input();
    if(choice != "Y" && choice != "y" && choice != "Yes" && choice != "yes"){
        cout << "You decided not to catch the " << found << ".\n";
        return;
    }
    // Check if the pokemon is already in the user's pokemons vector
    for(Pokemon p : user_pokemons){
        if(p == found){
            cout << "You already have a " << found << "!\n";
            return;
        }
    }
    int catch_chance = rng(3); // Random chance to catch the pokemon
    if(catch_chance != 0 && battled == false){ // 1/3 chance to catch if not battled
        cout << "The " << found << " escaped!\n";
        return;
    }else if(catch_chance == 0 && battled == true){ // 2/3 chance to catch if battled
        cout << "The " << found << " escaped!\n";
        return;
    }
    cout << "You caught the " << found << "!\n";
    user_pokemons.push_back(found); // Adds the found pokemon to the user's pokemons vector
}


// CORE FUNCTIONS
// Exploration function to find/catch pokemon
void exploring(){
    int find_chance = rng(2);
    if (find_chance == 0)
        cout << "\nYou didn't find anything.\n";
    else{
        cout << "\nYou found a wild Pokemon!\n";
        catching(wild_pokemons[rng(wild_pokemons.size())]);
    }
        
}


int type_advantage(Pokemon& attacker, Pokemon& defender){
    // Electric > Water, Water > Fire, Fire > Grass, Grass > Water

    if(attacker.type == "Electric" && defender.type == "Water"){
        defender.current_hp -= attacker.atk_power / 2;
    }else if(attacker.type == "Water" && defender.type == "Fire"){
        defender.current_hp -= attacker.atk_power / 2;
    }else if(attacker.type == "Fire" && defender.type == "Grass"){
        defender.current_hp -= attacker.atk_power / 2;
    }else if(attacker.type == "Grass" && defender.type == "Water"){
        defender.current_hp -= attacker.atk_power / 2;
        
    }else{
        cout << "It's only adequately effective\n\n";
        return defender.current_hp;
    }
    cout << "It's super effective!\n\n";
    if (defender.current_hp < 0)
        defender.current_hp = 0;
    return defender.current_hp;
}

string battling(Pokemon& user_pokemon, Pokemon& opponent){
    int max_atk_power = user_pokemon.atk_power;
    int opponent_max_atk_power = opponent.atk_power;

    while(user_pokemon.current_hp > 0 && opponent.current_hp > 0){
        cout << "\nYour " << user_pokemon << "'s HP: " << user_pokemon.current_hp << "/" << user_pokemon.max_hp << endl;
        cout << "Wild " << opponent << "'s HP: " << opponent.current_hp << "/" << opponent.max_hp << endl;
        cout << "\nChoose an action:"
            "\n(1) " << user_pokemon.atk_name <<
            "\n(2) " << user_pokemon.special_atk_name <<
            "\n(3) " << user_pokemon.status_move_name <<
            "\n(4) Run\n"
            "Action: ";
        int action;
        //cin >> action;
        action = num_input();
        cout << endl;

        if(action == Attack){
            user_pokemon.action(opponent, user_pokemon.atk_name);
            opponent.current_hp = type_advantage(user_pokemon, opponent);
        }else if(action == SpecialAttack){
            user_pokemon.action(opponent, user_pokemon.special_atk_name);
            opponent.current_hp = type_advantage(user_pokemon, opponent);
        }else if(action == StatusMove){
            user_pokemon.action(opponent, user_pokemon.status_move_name);
        }else if(action == Run){
            user_pokemon.atk_power = max_atk_power;
            return "Ran";
        }else{
            cout << "Invalid action! Turn skipped.\n";
        }

        if(opponent.current_hp > 0){
            // Opponent attacks back
            int opponent_choice = rng(3) + 1; // Random action between 1 and 3
            if(opponent_choice == 1){
                opponent.action(user_pokemon, opponent.atk_name);
                user_pokemon.current_hp = type_advantage(opponent, user_pokemon);
            }else if(opponent_choice == 2){
                opponent.action(user_pokemon, opponent.special_atk_name);
                user_pokemon.current_hp = type_advantage(opponent, user_pokemon);
            }else if(opponent_choice == 3)
                opponent.action(user_pokemon, opponent.status_move_name);
        }
    }
    // Health status after battle
    cout << "\nYour " << user_pokemon << "'s HP: " << user_pokemon.current_hp << "/" << user_pokemon.max_hp << endl;
    cout << "Wild " << opponent << "'s HP: " << opponent.current_hp << "/" << opponent.max_hp << endl;

    user_pokemon.atk_power = max_atk_power; // Reset user's attack power
    opponent.atk_power = opponent_max_atk_power; // Reset opponent's attack power

    if(user_pokemon.current_hp == 0){
        return "Lost";
    }else{
        return "Won";
    }
    
}

// Prepares the battle by selecting a random wild pokemon and allowing the user to choose their pokemon
void prepare_battle(){
    int random_index = rng(wild_pokemons.size());
    Pokemon opponent = wild_pokemons[random_index];
    cout << "\nYou encountered an angry, wild " << opponent << "!\n\n";


    if(user_pokemons.size()==0){
        cout << "You have no pokemons to battle with!\n";
        return;
    }
    cout << "(Enter 0 to Exit)\nChoose a pokemon to battle with:\n";
    for(int i=0; i<user_pokemons.size(); i++){
        cout << "(" << i+1 << ") " << user_pokemons[i] << " (Level " << user_pokemons[i].level << " | HP " << user_pokemons[i].current_hp << "/" << user_pokemons[i].max_hp << ")\n";
    }
    int choice;
    cout << "Choice: ";
    //cin >> choice;
    choice = num_input();
    if (choice == 0){
        cout << "Exiting battle menu.\n";
        return;
    }
    if(choice<1 || choice>user_pokemons.size()){
        cout << "Invalid Input\n";
        return;
    }
    Pokemon user_pokemon = user_pokemons[choice-1];
    cout << "You chose your " << user_pokemon << " (Level " << user_pokemon.level << ") to battle!\n";

    // Level up the opponent to make it a fair fight
    for(int i=0; i<user_pokemon.level -1; i++)
        opponent.level_up(true);
    
    // START BATTLE
    string outcome;
    outcome = battling(user_pokemon, opponent); 

    if(outcome == "Ran"){
        cout << "You ran away from the battle!\n";
        user_pokemons[choice-1] = user_pokemon; // Updates the user's pokemon with the new current HP
    }else if(outcome == "Lost"){
        cout << "\nYour " << user_pokemon << " has fainted! You lost the battle.\n";
    }else{
        cout << "\nYou defeated the wild " << opponent << "!\n";
        user_pokemon.level_up();
        catching(opponent, true); // Gives the user a chance to catch the defeated pokemon
    }
    user_pokemons[choice-1] = user_pokemon; // Updates the user's pokemon with the new current HP and potentially level
}

void healing(){
    if(user_pokemons.size()==0){
        cout << "\nYou have no pokemons to heal!\n";
        return;
    }
    cout << "\n(Enter 0 to Exit)\nChoose a pokemon to heal:\n";
    for(int i=0; i<user_pokemons.size(); i++){
        cout << "(" << i+1 << ") " << user_pokemons[i] << " (HP " << user_pokemons[i].current_hp << "/" << user_pokemons[i].max_hp << ")\n";
    }

    int choice;    
    cout << "Choice: ";
    //cin >> choice;
    choice = num_input();
    if(choice == 0){
        cout << "Exiting heal menu.\n";
        return;
    }
    if(choice<1 || choice>user_pokemons.size()){
        cout << "\nInvalid Input\n";
        return;
    }

    user_pokemons[choice-1].heal();
}

void see_pokemon(){
    if(user_pokemons.size()==0){
        cout << "\nYou have no pokemon!\n";
        return;
    }
    cout << "\nYour Pokemons:\n";
    for(int i=0; i<user_pokemons.size(); i++){
        cout << "\n(" << i+1 << ")\n";
        user_pokemons[i].display_info();
    }
}

bool start(){
    cout << "\nChoose your starting Pokemon:\n"
        "(1) Bulbasaur (Grass)\n"
        "(2) Charmander (Fire)\n"
        "(3) Squirtle (Water)\n"
        "(4) Pikachu (Electric)\n"
        "(5) None\n";
    
    int choice;
    cout << "Choice: ";
    //cin >> choice;
    choice = num_input();

    Pokemon start_pokemon;
    if(choice == 1)
        start_pokemon = {"Bulbasaur", "Grass", 5, 65, 65, 17, "Vine Whip", "Solar Beam", "Leech Seed"};
    else if(choice == 2)
        start_pokemon = {"Charmander", "Fire", 5, 59, 59, 20, "Ember", "Flamethrower", "Smokescreen"};
    else if(choice == 3)
        start_pokemon = {"Squirtle", "Water", 5, 64, 64, 19, "Water Gun", "Hydro Pump", "Bubble"};
    else if(choice == 4)
        start_pokemon = {"Pikachu", "Electric", 5, 55, 55, 18, "Thunder Shock", "Thunderbolt", "Tail Whip"};
    else if(choice == 5){
        cout << "\nYou chose to begin without a starting Pokemon.\n";
        return true;
    }else{
        cout << "\nInvalid Input\n";
        return false;
    }
    user_pokemons.push_back(start_pokemon);
    cout << "\nYou chose " << start_pokemon << " as your starting Pokemon!\n";
    return true;
}

int main(){ // This welcomes the user and lets the user choose to use or exit the program.

    cout << "\n\nWelcome to this Pokemon Program, which lets you explore and capture, find and fight, pick and heal, and see status of pokemon.\n(Enter 10 in the Menu for Help)\n";
    
    while (true){ // Keep asking until a valid pokemon is chosen
        if(start() == true)
            break;
    }

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

        //cin >> choice;
        choice = num_input();

        if (choice == Explore){
            exploring();
        }else if(choice == Battle){
            prepare_battle();
        }else if(choice == Heal){
            healing();
        }else if(choice == YourPokemon){
            see_pokemon();
        }else if(choice == Exit){
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else if(choice == 10){ // Help Menu
            cout << "\n\nHelp Menu:"
                "\n(1) Explore: Find and catch wild Pokemon."
                "\n(2) Battle: Fight against wild Pokemon to level up your Pokemon."
                "\n(3) Heal: Restore your Pokemon's health."
                "\n(4) Your Pokemon: View your current Pokemon and their stats."
                "\n(5) Exit: Leave the game.\n"
                "\nType Advantages:\nElectric > Water\nWater > Fire\nFire > Grass\nGrass > Water\n\n";
        }else{
            cout << "\nInvalid Input\n";;
        }
    }
    return 0;
}

// Check that it isn't all Copilot-y
// Check for Rubric
// Test

// Follow RUBRIC