// LM  Text Files Notes

#include <iostream> // Input and Output (i and o streams)
#include <limits>
#include <fstream> // read and write (if and of streams) [input and output]
#include <iomanip>
#include <string>
#include <vector>

using namespace std;


struct Movie{
    int id;
    string title;
    int year;
};


int getNumber(const string& prompt){
    int num;
    while (true){
        cout << prompt;
        cin >> num;
        if(cin.fail()){
            cout << "Enter a valid number!\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
        }else break;
    }
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer
    return num;
}


int main(){

    /*
    terminal - cout, cin (User given)
    file - txt, csv, binary
    network - internet, other computers
    */

    int first = getNumber("First: \n");
    int second = getNumber("Second: \n");

    cout << "You entered " << first << " and " << second << endl;



    // FILES
    /*
    ifstream > input files stream
    ofstream < output file stream
    fstream >< combines the functionality
    */

    // TXT
    // writing
    ofstream ofile;
    ofile.open("data.txt");
    if(ofile.is_open()){
        ofile << setw(20) << "Hello " << setw(20) << "World";
        ofile.close();
    }

    // // reading
    // ifstream file;
    // file.open("data.txt");
    // if(file.is_open()){
    //     string str;
    //     file >> str;
    //     cout << str << endl;
    //     file.close();
    // }


    // CSV
    // writing
    ofile.open("data.csv");
    if(ofile.is_open()){
        ofile << "id, title, year\n" // 'endl' clears the buffer but '\n' does not
        << "1,Terminator 1,1984\n"
        << "2,Terminator 2,1991\n";
        ofile.close();
    }
            
    // reading
    ifstream ifile;
    ifile.open("data.csv");
    string line;
    vector<Movie> movies;

    if(ifile.is_open()){
        getline(ifile,line);

        while(getline(ifile,line)){
            istringstream iss(line);
            string item;

            Movie movie;
            getline(iss, item, ',');
            movie.id = stoi(item);
            getline(iss, item, ',');
            movie.title = item;
            getline(iss, item, ',');
            movie.year = stoi(item);

            movies.push_back(movie);
        }
        ifile.close();

        for(Movie i: movies){
            cout << i.title << endl;
        }
    }

    return 0;
}



// NOTES QUESTIONS


// What are the 3 main sources of data for a program
    // They are terminal, file, and network.

// What are streams?
    // They are a source of data or a destination for data.

// What are the different streams we might need to include in a program? 
    // istream and ostream

// What is the base class for all streams?
    // ios_base

// What is buffer?
    // A temporary holder of what the user has inputted to will then be put in a variable. (cin >> variable)

// How do you clear the buffer?
    // cin.ignore(num_of_characters, char_to_stop_at)
    // cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Clears the buffer (Clears the specified amount of characters or up to \n)

// How do you handle invalid inputs from the terminal
    // Using the getNumber function seen above


// What streams are for files specifically
    // ifstream > input files stream
    // ofstream < putput file stream
    // fstream >< combines the functionality

// How do you write to a text file?
    // Using ofstream
    // Seen Above

// What do stream manipulators let us do?
    // Lets us adjust the formatting of how we are writing information to the file
    // Like putting them in columns

// How do you write to a CSV?
    // Same way as txt files basically

// How do you read a text file?
    // Same way that you read a CSV file basically (without separating commas I guess)

// How do you read a CSV file?
    // Using ifstream
    // Seen Above

// What is a delimiter?
    // The character that divides your pieces of data

// How do you read an entire CSV?
    // Using loops and 'file >>' or getline()

// How do you turn items from a CSV into objects of a structure?
    // Example:
        // ifstream ifile;
        // ifile.open("data.csv");
        // string line;
        // vector<Movie> movies;

        // if(ifile.is_open()){
        //     getline(ifile,line);
        //     while(getline(ifile,line)){
        //         istringstream iss(line);
        //         string item;

        //         Movie movie;
        //         getline(iss, item, ',');
        //         movie.id = stoi(item);
        //         getline(iss, item, ',');
        //         movie.title = item;
        //         getline(iss, item, ',');
        //         movie.year = stoi(item);

        //         movies.push_back(movie);
        //     }
        //     ifile.close();

        //     for(Movie i: movies){
        //         cout << i.title << endl;
        //     }
        // }