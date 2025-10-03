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

RUBRIC:
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
    string title;
    string director;
    int year;
    string genre;
    string rating;
};

string user_file = "";
vector<Movie> movies; // Vector to hold the scores


int getNumber(const string& prompt){ // Gets a valid integer from the user
    int num;
    while (true){
        cout << prompt;
        cin >> num;
        if(cin.fail()){
            cout << "\nInvalid Input (Enter a valid number!)\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
        }else break;
    }
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
    return num;
}

string getString(const string& prompt){ // Gets a valid string from the user
    string str;
    while (true){
        cout << prompt;
        getline(cin, str);

        if (cin.fail()  ||  str.empty()  ||  str.find(',') != string::npos){ // Checks for invalid input (empty or contains a comma [commas mess up the CSV])
            cout << "\nInvalid Input (Enter a valid input! [No commas allowed])\n";
        }else break;
    }
    return str;
}


void read_file(){ // Reads the scores from the file into the vector
    
    movies.clear(); // Clears the vector before reading the file
    
    ifstream ifile;
    ifile.open(user_file);
    string line;

    if(ifile.is_open()){
        getline(ifile,line);

        while(getline(ifile,line)){
            istringstream iss(line);
            string item;

            Movie temp_movie;
            getline(iss, item, ',');
            temp_movie.title = item;
            getline(iss, item, ',');
            temp_movie.director = item;
            getline(iss, item, ',');
            temp_movie.year = stoi(item);
            getline(iss, item, ',');
            temp_movie.genre = item;
            getline(iss, item, ',');
            temp_movie.rating = item;

            movies.push_back(temp_movie);
        }
        ifile.close();
    }
}

void write_file(){ // Writes the scores from the vector into the file
    ofstream ofile;
    ofile.open(user_file);
    if(ofile.is_open()){
        ofile << "Title,Director,Year,Genre,Rating\n"; // Header
        for(const Movie &m: movies){
            ofile << m.title << "," << m.director << "," << m.year << "," << m.genre << "," << m.rating << endl;
        }
        ofile.close();
    }
}


void load_file(){
    user_file = getString("\nEnter the filename to load (e.g., movies.csv): ");

    ifstream ifile(user_file);
    if(!ifile){
        cout << "\nFile Not Found\n";
        user_file = "";
        ifile.close();
        return;
    }
    ifile.close();
    cout << "\nFile Loaded Successfully!\n";
    read_file();
}

void view(int index){ // Displays a single movie
    cout << index + 1 << ". Title: " << movies[index].title 
                    << " | Director: " << movies[index].director
                    << " | Year: " << movies[index].year
                    << " | Genre: " << movies[index].genre
                    << " | Rating: " << movies[index].rating << endl;
    
                    // int index = getNumber("\nEnter the movie number to view: ") - 1;

    // if(index < 0 || index >= movies.size()){
    //     cout << "\nInvalid Movie Number\n";
    //     return;
    // }

    // cout << "\nMovie Details:\n";
    // cout << "Title: " << movies[index].title << endl;
    // cout << "Director: " << movies[index].director << endl;
    // cout << "Year: " << movies[index].year << endl;
    // cout << "Genre: " << movies[index].genre << endl;
    // cout << "Rating: " << movies[index].rating << endl;

}

void view_all(){ // Displays the movies in the vector
    cout << "\nMovie Library:\n\n";

    if(movies.empty()) {
        cout << "\t[Empty]\n\nAdd movies to this library first\n";
        return;
    }

    for(int i = 0; i < movies.size(); ++i){
        view(i);
    }
}

void add_movie(){ // Adds a new movie to the vector and file

    Movie new_movie;
        new_movie.title = getString("\nEnter movie title: ");
        new_movie.director = getString("\nEnter director: ");
        new_movie.year = getNumber("\nEnter release year: ");
        new_movie.genre = getString("\nEnter genre: ");
        new_movie.rating = getString("\nEnter rating (e.g., G, PG, PG-13, R): ");

    movies.push_back(new_movie);
    write_file();
    cout << "\nHigh Score Successfully Added!\n";
}

void delete_movie(){
    // int index = getNumber("\nEnter the movie number to delete: ") - 1;

    // if(index < 0 || index >= movies.size()){
    //     cout << "\nInvalid Movie Number\n";
    //     return;
    // }

    // char confirm;
    // cout << "\nAre you sure you want to delete \"" << movies[index].title << "\"? (y/n): ";
    // cin >> confirm;
    // cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer

    // if(tolower(confirm) == 'y'){
    //     movies.erase(movies.begin() + index);
    //     write_file();
    //     cout << "\nMovie Successfully Deleted!\n";
    // }else{
    //     cout << "\nDeletion Cancelled.\n";
    // }
}

void search_movie(){
    // while(true){
    //     string criteria = getString(
    //         "\nSearch Menu:\n"
    //         "(1) Rating\n"
    //         "(2) Director\n"
    //         "(3) Release Year\n"
    //         "(4) Genre\n"
    //         "Choice: ");

    //     string value;
    //     vector<int> results;
    //     if(criteria == "1"){
    //         value = getString("\nEnter rating to search for (e.g., G, PG, PG-13, R): ");
    //         for(int i = 0; i < movies.size(); ++i){
    //             if(movies[i].rating == value){
    //                 results.push_back(i);
    //             }
    //         }
    //     }else if(criteria == "2"){
    //         value = getString("\nEnter director to search for (e.g., Christopher Nolan): ");
    //         for(int i = 0; i < movies.size(); ++i){
    //             if(movies[i].director == value){
    //                 results.push_back(i);
    //             }
    //         }
    //     }else if(criteria == "3"){
    //         int year = getNumber("\nEnter release year to search for (e.g., 1987): ");
    //         for(int i = 0; i < movies.size(); ++i){
    //             if(movies[i].year == year){
    //                 results.push_back(i);
    //             }
    //         } 
    //     }else if(criteria == "4"){
    //         value = getString("\nEnter genre to search for (e.g., Action, Comedy): ");
    //         for(int i = 0; i < movies.size(); ++i){
    //             if(movies[i].genre == value){
    //                 results.push_back(i);
    //             }
    //         }
    //     }else{
    //         cout << "\nInvalid Input (Enter an integer 1-4)\n";
    //         return;
    //     }
    // }
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
        
        if(user_file == "" && choice > 1 && choice < 6){
            cout << "\nYou must load a file first!\n";
            continue;
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


// Implement everything