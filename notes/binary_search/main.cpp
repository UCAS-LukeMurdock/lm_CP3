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
    // 

// Why might extra zeros be added to a string when converting a value without control?
    // 

// How does controlling the string conversion process benefit your program?
    // 

// Give an example scenario where parsing a string would be necessary in a program.
    // 

// Why are images, audio, and PDFs not readable by humans when stored in files?
    // 

// What file extensions are commonly used to create binary files?
    // 

// When writing to a binary file, what does the first parameter (reinterpret_cast<char*>(&numbers)) represent?
    // 

// Why does the binary file only take 12 bytes while the array of integers might be larger?
    // 

// How does reading individual numbers from a binary file differ from reading the entire list at once?
    // 

// What is the main difference between sequential search and binary search?
    // 

// In which type of data structure is binary search most efficient?
    // 

// What is a key requirement for binary search to work correctly on a list?
    // 

// How does sequential search find an item in a list?
    // 

// Why is binary search generally faster than sequential search for large, sorted lists?
    // 
