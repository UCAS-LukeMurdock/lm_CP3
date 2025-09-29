// LM  Program

#include <iostream>
#include <string>

using namespace std;

/*
Write a program that manages a high score leaderboard for a game using file I/O in C++.
The program should allow the user to add new high scores, view the existing leaderboard, and save the data to a text file.
It should also read data from the file when the program starts.
The user menu should include options to add a new score, display the high scores, and exit.
The program must handle invalid inputs gracefully and continue running until the user chooses to exit.

OUTPUT EXAMPLE: 

    High Score Leaderboard:

    1. Player: Alice | Score: 1200 | Date: 09/26/2025
    2. Player: Bob   | Score: 950  | Date: 09/25/2025
    3. Player: Carol | Score: 880  | Date: 09/24/2025

    Menu:
    1. Add a new high score
    2. Display high scores
    3. Exit
    Enter your choice (1-3): 1

    Enter player's name: Alice
    Enter score: 1300
    Enter date (MM/DD/YYYY): 09/26/2025

    High score added successfully.

    Menu:
    1. Add a new high score
    2. Display high scores
    3. Exit
    Enter your choice (1-3): 2

    --- High Scores ---
    1. Player: Alice | Score: 1300 | Date: 09/26/2025
    2. Player: Alice | Score: 1200 | Date: 09/26/2025
    3. Player: Bob   | Score: 950  | Date: 09/25/2025
    4. Player: Carol | Score: 880  | Date: 09/24/2025

    Menu:
    1. Add a new high score
    2. Display high scores
    3. Exit
    Enter your choice (1-3): 3

    Goodbye!

KEY REMINDERS:
    Use appropriate data structures, such as struct or class, to store the high score data.
    When adding a new score, insert it into the list, and sort based on scores if necessary.
    When the program starts, read existing high scores from a text file (e.g., highscores.txt) and load them into memory.
    When the program exits, save the current high scores back to the file, overwriting previous data if needed.
    Use fstream for file input/output, and ensure proper opening, reading, writing, and closing files.
    Implement input validation for menu choices, scores, and date formats.
    Make sure your program continues to run until the user chooses to exit.

RUBRIC:
    File Reading:  Correctly reads and parses existing high scores from the text file upon program start without errors.
    File Writing:  Successfully saves all high score data to the text file upon exit, maintaining correct format and ordering.
    Data Persistence:  Data read at program start and saved upon exit, maintaining data integrity across sessions.
    Proper File Handling:  Files are opened, read, and closed appropriately with error handling for file operations.
    Implementation of Sorting/Updating:  Correctly updates and sorts high scores in the file, maintaining order based on scores.
*/

// Enumeration for the menu options
enum Menu{
    Add = 1,
    Display,
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
        "(1) Add\n"
        "(2) Display\n"
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