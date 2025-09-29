// LM  Text Files Notes

#include <iostream> // Input and Output (i and o streams)
#include <limits>
#include <fstream> // read and write (if and of streams) [input and output]
#include <iomanip>

using namespace std;


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

    cout << "You entered " << first << " and " << second;


    /*
    ifstream > input files stream
    ofstream < output file stream
    fstream >< combines the functionality
    */
    ofstream file;
    file.open("data.txt");
    if(file.is_open()){
        file << setw(20) << "Hello " << setw(20) << "World";
        file.close();
    }

    file.open("data.csv");
    if(file.is_open()){
        file << "id, title, year\n"
        << "1, Terminator 1, 1984\n"
        << "2, Terminator 2, 1991\n";
        file.close();
    }
    // endl clears the buffer but \n does not

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
    // A temporary holder that holds what the user has inputted

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

// What do stream manipulators let us do?
    // Lets us adjust the formatting of how we are writing information to the file
    // Like putting them in columns

// How do you write to a CSV?
    // Same way as txt

// How do you read a text file?
    // 

// How do you read a CSV file?
    // 

// What is a delimiter?
    // 

// How do you read an entire CSV?
    // 

// How do you turn items from a CSV into objects of a structure?
    // 
