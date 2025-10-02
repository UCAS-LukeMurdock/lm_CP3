// LM  Movie Library Program

#include <iostream> // Input and Output (i and o streams)
#include <limits>
#include <fstream> // read and write (if and of streams) [input and output]
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

/*
INSTRUCTIONS:
Create an application that manages your Movie Library using structures to store movie details and enumerations for menu options. Your program should persist movie data by reading from and writing to an external file in CSV format.

Main menu needs to allow our user to load the library from a file (I will use a different one than the example one I have given you), view all movies, add a movie, delete a movie, and search movies.

The search menu should allow the user to select what they would like to search by, then the specific value they would like to search. 

NOTE: You need to build a sequential search algorithm for this project (it is a state standard) 

NOTE: Practice Movies ListDownload Practice Movies List

EXAMPLE:
Rating (e.g., G, PG, PG-13, R)
Director (e.g., Christopher Nolan)
Release Year (e.g., 1987)
Genre (e.g., Action, Comedy)
KEY REMINDERS:
Use structures to organize movie data.
Use enumerations for the menu.
Incorporate input validation and error handling.
Make sure the program is user-friendly and clear.

Use of Structures to Store Movie Data:  All movie details are stored correctly using appropriate structures.
Use of Enumerations for Menu Options:  Implemented using enumerations accurately, enhancing clarity.
File Reading/Writing in CSV Format:  Correctly reads from and writes to CSV, data persists accurately.
Load Data from File:  Properly loads data into library from CSV file.
Add a Movie:  Users can add movies correctly with input validation; data stored properly.
Delete a Movie:  Reliable deletion with confirmation and validation.
Sequential Search:  Search by criteria works correctly; results displayed appropriately.
User-Friendliness & Clarity:  Clear, intuitive, and user-friendly interface.
*/





// Enumeration for the menu options
enum Menu{
    Load = 1,
    View,
    Add,
    Delete,
    Search,
    Exit
};

// Structure to hold a movie
struct Movie{
    // string name;
    // int score;
    // string date;
};

string user_file = "";
vector<Movie> movies; // Vector to hold the scores


int getNumber(const string& prompt){ // Gets a valid integer from the user
    int num;
    while (true){
        cout << prompt;
        cin >> num;
        if(cin.fail()){
            cout << "\nInvalid Input\nEnter a valid number!\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
        }else break;
    }
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
    return num;
}

string getString(const string& prompt, bool date = false){ // Gets a valid string from the user (or date if specified)
    string str;
    while (true){
        cout << prompt;
        getline(cin, str);

        if (cin.fail()  ||  str.empty()  ||  str.find(',') != string::npos){ // Checks for invalid input (empty or contains a comma [commas mess up the CSV])
            cout << "\nInvalid Input\nEnter a valid input!\n";
        }else if(date == true // If the input is supposed to be a date then it checks for valid date format (MM/DD/YYYY)
        && (str.length() != 10 || str[2] != '/' || str[5] != '/' 
        || stoi(str.substr(0,2)) < 1 || stoi(str.substr(0,2)) > 12
        || stoi(str.substr(3,2)) < 1 || stoi(str.substr(3,2)) > 31
        || stoi(str.substr(6,4)) < 0 || stoi(str.substr(6,4)) > 2025) ){
            
            cout << "\nInvalid Input\nPlease use MM/DD/YYYY format!\n";
            str.clear();
            
        }else break;
    }
    return str;
}


void read_file(){ // Reads the scores from the file into the vector
    ifstream ifile;
    ifile.open(user_file);
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
    ofile.open(user_file);
    if(ofile.is_open()){
        ofile << "Movie Name,Director,Year,Genre,Rating\n"; // Header
        for(const Score &s: scores){
            ofile << s.name << "," << s.score << "," << s.date << endl;
        }
        ofile.close();
    }
}




void display_scores(){ // Displays the scores in the vector
    cout << "\nHigh Scores Leaderboard:\n\n";

    if(scores.empty()) {
        cout << "\t[Empty]\n\nNo High Scores Yet!\n";
        return;
    }

    for(int i = 0; i < scores.size(); ++i){
        cout << i + 1 << ". Player: " << scores[i].name 
                    << " | Score: " << scores[i].score 
                    << " | Date: " << scores[i].date << endl;
    }
}

void load_file(){

    read_file(user_file);
}

void view(){

}

void view_all(){ // Displays the movies in the vector
    cout << "\nMovie Library:\n\n";

    if(movies.empty()) {
        cout << "\t[Empty]\n\nNo High Scores Yet!\n";
        return;
    }

    for(int i = 0; i < scores.size(); ++i){
        cout << i + 1 << ". Player: " << scores[i].name 
                    << " | Score: " << scores[i].score 
                    << " | Date: " << scores[i].date << endl;
    }
}

void add_movie(){ // Adds a new movie to the vector and file

    Movie new_movie;
    new_movie.name = getString("\n(Do not enter any commas)\nEnter player's name: ");
    new_movie.score = getNumber("\nEnter score: ");
    new_movie.date = getString("\n(Example: MM/DD/YYYY)\nEnter date: ", true);
    
    movies.push_back(new_movie);
    write_file();
    cout << "\nHigh Score Successfully Added!\n";
}

void delete_movie(){
    
}

void search_movie(){
    
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this Movie Library Program, which lets you load a CSV file of movies, view them all, add a new one, delete one, and search through the movies.\n";

    while(true){
        int choice = getNumber(
            "\nMenu:\n"
            "(1) Load File\n"
            "(2) View All\n"
            "(3) Add Movie\n"
            "(4) Delete Movie\n"
            "(5) Search Movie\n"
            "(6) Exit\n"
            "Choice: ");
        
        if(user_file == "" && choice >= 1 && choice <= 6){
            cout << "\n";
            
        }

        if (choice == Load){
            load_file();
        }else if(choice == View){
            view_all();
        }else if(choice == Add){
            add_movie();
        }else if(choice == Delete){
            delete_movie();
        }else if(choice == Search){
            search_movie();
        }else if(choice == Exit){
            cout << "\n\n\nCome Back Soon!\n\n\n";
            break;
        }else{
            cout << "\nInvalid Input (Enter an integer 1-6)\n";;
        }
    }
    return 0;
}

// Transform
// Add Saving Everywhere (Writing)
// Add to Template


// Movie Name,Director,Year,Genre,Rating