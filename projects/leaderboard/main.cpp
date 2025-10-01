// LM  High Score Leaderboard Program

#include <iostream> // Input and Output (i and o streams)
#include <limits>
#include <fstream> // read and write (if and of streams) [input and output]
#include <iomanip>
#include <string>
#include <vector>

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


struct Score{
    string name;
    int score;
    string date;
};

vector<Score> scores; // Vector to hold the scores


int getNumber(const string& prompt){
    int num;
    while (true){
        cout << prompt;
        cin >> num;
        if(cin.fail()){
            cout << "\nEnter a valid number!\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
        }else break;
    }
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
    return num;
}

string getString(const string& prompt){
    string str;
    while (true){
        cout << prompt;
        cin >> str;
        cin.ignore();
        getline(cin,str);
        if(cin.fail()){
            cout << "\nInvalid Input!\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
        }else break;
    }
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
    return str;
}

// float num_input(){ // Checks if the input is valid (It needs to be a number [float])
//     float input;
//     while (!(cin >> input)){
//         cin.clear(); // clear error state
//         cin.ignore(10000, '\n'); // discard invalid input completely
//         cout << "\nInvalid Input Type (Enter in a Number)\nNew Input: ";
//     }
//     return input;
// }

// Checks inputs to make sure they don't fail
// void check_input(){
//     if(cin.fail()){
//         cin.clear(); // clear error state
//         cin.ignore(10000, '\n'); // discard invalid input completely
//     }
// }


void read_file(){ // Reads the scores from the file into the vector
    ifstream ifile;
    ifile.open("scores.csv");
    string line;

    if(ifile.is_open()){
        getline(ifile,line);

        while(getline(ifile,line)){
            istringstream iss(line);
            string item;

            Score temp_score;
            getline(iss, item, ',');
            temp_score.name = item;
            getline(iss, item, ',');
            temp_score.score = stoi(item);
            getline(iss, item, ',');
            temp_score.date = item;

            scores.push_back(temp_score);
        }
        ifile.close();
    }
}

void write_file(){ // Writes the scores from the vector into the file
    ofstream ofile;
    ofile.open("scores.csv");
    if(ofile.is_open()){
        for(const Score &s: scores){
            ofile << s.name << "," << s.score << "," << s.date << endl;
        }
        ofile.close();
    }
}

void sort_scores(){ // Sorts the scores in descending order

    for(int i = 0; i < scores.size(); ++i){
        for(int j = i + 1; j < scores.size(); ++j){
            // Checks to see if the further number is greater than the closer number and if it is then it will come closer to first place.
            if(scores[j].score > scores[i].score){
                swap(scores[i], scores[j]);
            }
        }
    }
}

void add_score(){ // Adds a new score to the vector

    Score new_score;
    cout << "\nEnter player's name: ";
    cin >> new_score.name;
    // -------------------------

    new_score.score = getNumber("\nEnter score: ");

    cout << "\nEnter date (MM/DD/YYYY): ";
    cin >> new_score.date;
    // -------------------------
    
    scores.push_back(new_score);
    cout << "\nHigh Score Successfully Added!\n";
}

void display_scores(){ // Displays the scores in the vector
    cout << "\nHigh Scores Leaderboard:\n";

    for(int i = 0; i < scores.size(); ++i){
        cout << i + 1 << ". Player: " << scores[i].name 
            << " | Score: " << scores[i].score 
            << " | Date: " << scores[i].date << endl;
    }
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this High Score Leaderboard Program, which lets you add new high scores and see the leaderboard.\n";
    read_file(); // Read existing scores from file
    display_scores(); // Display existing scores
    
    while(true){
        int choice = getNumber("\nMenu:\n"
                            "(1) Add Score\n"
                            "(2) Display Leaderboard\n"
                            "(3) Save & Exit\n"
                            "Choice: ");

        if (choice == Add){
            add_score();
            sort_scores();
            display_scores();
        }else if(choice == Display){
            display_scores();
        }else if(choice == Exit){
            write_file();
            cout << "\n\n\nCome Back Soon!\n\n\n" << endl;
            break;
        }else{
            cout << "\nInvalid Input (Enter an Integer 1-3)\n";;
        }
    }
    return 0;
}

// Fix functionality (Inputs)
// Understand sort
// de-Copilot it