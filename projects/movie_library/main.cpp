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

// For Search Menu Options
enum Search_Menu{
    Title = 1,
    Director,
    Year,
    Genre,
    Rating,
    Stop
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
            cout << "\nInvalid Input (Enter a valid input! [No commas allowed, Check capitalization and spelling])\n";
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
    user_file = getString("\n(Example: movies.csv)\nEnter the filename to load: ");

    ifstream ifile(user_file);
    if(!ifile){
        cout << "\nFile Not Found\nNo Current Loaded File\n";
        user_file = "";
        ifile.close();
        return;
    }
    ifile.close();
    read_file();
    cout << "\nFile Loaded Successfully!\n";
}

void view(int index){ // Displays a single movie
    cout << index + 1 << ". Title: " << movies[index].title 
                    << " | Director: " << movies[index].director
                    << " | Year: " << movies[index].year
                    << " | Genre: " << movies[index].genre
                    << " | Rating: " << movies[index].rating << endl;
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
        new_movie.rating = getString("\n(Examples: G, PG, PG-13, R)\nEnter rating: ");

    movies.push_back(new_movie);
    write_file();
    cout << "\nNew Movie Successfully Added!\n";
}

void delete_movie(){
    int index = getNumber("\nEnter the movie number to delete: ") - 1;

    if(index < 0 || index >= movies.size()){
        cout << "\nInvalid Movie Number (Find the movie number of the movie you want deleted by either viewing or searching through the movies)\n";
        return;
    }

    char confirm;
    cout << "\nAre you sure you want to delete \"" << movies[index].title << "\"? (Y/N): ";
    cin >> confirm;
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer

    if(toupper(confirm) == 'Y'){
        movies.erase(movies.begin() + index);
        write_file();
        cout << "\nMovie Successfully Deleted!\n";
    }else{
        cout << "\nDeletion Cancelled\n";
    }
}


vector<int> search_movie(int choice, string& category){
    string user_search;
    int int_user_search;
    vector<int> results;
    cout << "\nSearching For " << category;
    if (choice == Year)
        int_user_search = getNumber("\nEnter what you want to search for: ");
    else
        user_search = getString("\nEnter what you want to search for: ");
    

    size_t found_pos;
    for(int i = 0; i < movies.size(); ++i){
        if(choice == Title){
            found_pos = movies[i].title.find(user_search);
            if (found_pos != string::npos) 
                results.push_back(i);
        }else if(choice == Director){
            found_pos = movies[i].director.find(user_search);
            if (found_pos != string::npos) 
                results.push_back(i);
        }else if(choice == Year && movies[i].year == int_user_search)
            results.push_back(i);
        else if(choice == Genre){
            found_pos = movies[i].genre.find(user_search);
            if (found_pos != string::npos) 
                results.push_back(i);
        }else if(choice == Rating && movies[i].rating == user_search)
            results.push_back(i);
    }
    return results;
}

void search_menu(){
    while(true){
        int choice = getNumber(
            "\nSearch Menu:\n"
            "(1) Title\n"
            "(2) Director\n"
            "(3) Release Year\n"
            "(4) Genre\n"
            "(5) Rating\n"
            "(6) Exit Searching\n"
            "Choice: ");

        string category;

        if(choice == Title){
            category = "Title\n(Example: The Iron Giant)";
        }else if(choice == Director){
            category = "Director\n(Example: Christopher Nolan)";
        }else if(choice == Year){
            category = "Release Year\n(Example: 1987)";
        }else if(choice == Genre){
            category = "Genre\n(Examples: Action, Comedy)";
        }else if(choice == Rating){
            category = "Rating\n(Examples: G, PG, PG-13, R)";
        }else if(choice == Exit){
            cout << "\nExiting Search Menu\n";
            return;
        }else{
            cout << "\nInvalid Input (Enter an integer 1-6)\n";
            continue;
        }
        vector<int> results = search_movie(choice, category);

        cout << "\nMovie Results:\n\n";
        if(results.empty()) {
            cout << "\t[None]\n\nPlease enter a correct detail that is in an existing movie within this movie library. (Check capitalization and spelling)\n";
            return;
        }
        for (int index: results){
            view(index);
        }
    }
}



int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this Movie Library Program, which lets you load a file (CSV) of movies, view them all, add a new one, delete one, and search through the movies.\n";

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
            search_menu();
        }else if(choice == Exit){
            cout << "\n\n\nCome Back Soon!\n\n\n";
            break;
        }else{
            cout << "\nInvalid Input (Enter an integer 1-6)\n";
        }
    }
    return 0;
}



// delete by title