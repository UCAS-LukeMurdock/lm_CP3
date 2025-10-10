// LM  Binary and Searching Notes

#include <iostream>
#include <fstream>
#include <iomanip> // Manipulating inputs and outputs
#include <sstream>
// #include <string>

/* Convert other data types to strings!
istringstream => reading a string
ostringstream => writing a string
stringstream => both!
*/

using namespace std;


struct Movie{
    string title;
    int year;
};

string to_string(double number, int precision){\
    stringstream stream;
    stream << fixed << setprecision(precision) << number;
    return stream.str();
}

Movie parseMovie(string str){
    stringstream stream;
    stream.str(str); // Putting the str variable into the parser
    // Ready to split

    Movie movie;
    getline(stream, movie.title, ','); // Make it now split by ','
    stream >> movie.year; // Puts the rest into year
    return movie;
}

int main(){
    double number = 3.14;
    // string str = to_string(number); // Uncontrolled conversion
    cout << to_string(number, 2) << endl;

    // Parsing
    string users = "10 20";
    stringstream fix;
    fix.str(users);
    int first;
    fix >> first;

    int second;
    fix >> second;

    cout << "First: " << first << "\nSecond: " << second << endl;

    auto movie = parseMovie("Terminator 1,1984");
    cout << "\nTitle: " << movie.title << "\nYear: " << movie.year << endl;


    fstream file;
    file.open("file.txt", ios::in | ios::out | ios::app); // Lets the file be readable, writable, and appendable.
    if (file.is_open()){

        file.close();
    }

    // if (const auto& person : people) {
    //     outFile.write(reinterpret_cast<const char*>(&person), sizeof(Person))
    // }


    cout << "\n";

    return 0;
}


// NOTES QUESTIONS


// What is a potential issue with converting values to strings without control?
    // It will add things you don't want like 0's.

// How can you control the way a value is converted to a string?
    // Using streamstream will help you control how it will be converted into a string.

// Why is it useful to create a reusable function for converting values to strings?
    // So then you can use it multiple times and don't have to control the converting everytime.

// What is parsing in the context of working with strings?
    // Parsing is extracting a piece of information from a string.

// How do you extract specific information from a string in programming?
    // You use stringstream to put the string into a stream that you then extract the different parts of it into variables (spacing is the default delimiter).
    // Seen Above

// When a title contains a space, which function should you use to read it properly?
    // getline()

// Why might extra zeros be added to a string when converting a value without control?
    // Becuase it is filling in for the spaces it has saved. It includes the implied 0s when it grabs it all.

// How does controlling the string conversion process benefit your program?
    // It lets us control how our stuff is being saved in our string.
    // It makes it give you what you want instead of random stuff.

// Give an example scenario where parsing a string would be necessary in a program.
    // When pulling information in from files and sometimes user inputs.

// When writing to a binary file, what does the first parameter (reinterpret_cast<char*>(&numbers)) represent?
    // It grabs the information and changes it to and from binary depending on the direction. It turns the data form binary back into our characters.
    // Converts from binary to the data type you want.

// Why does the binary file only take 12 bytes while the array of integers might be larger?
    // Becuase binary doesn't hold what the data is, it just holds what is inside of it.

// What is the main difference between sequential search and binary search?
    // Binary search needs the list to be ordered.
    // Sequential search takes up a lot more memory becuase the bigger the list the longer it takes.

// In which type of data structure is binary search most efficient?
    // Any sort of list.
    // Large, ordered lists are the best.

// What is a key requirement for binary search to work correctly on a list?
    // It only works properly with lists that are sorted/ordered.

// How does sequential search find an item in a list?
    // It compares every single item in the list to the one you are trying to find from the first to the last.

// Why is binary search generally faster than sequential search for large, sorted lists?
    // It cancels out a lot more possibilities (about half) every comparison.
    // Binary grabs the lenght of the list and then goes to the halfway point (the greater side if even) and then checks if the number is smaller or greater, then checks the next half and keeps on going.
