// LM  Structure Notes

#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Date{
    short year = 1900;
    short month = 1;
    short day = 1;
};

struct Movie { // PascalCase

    // Properties of the object
    // camelCase
    string title; // Declared
    Date releaseDate; // Intialized also
    bool isPopular = true;

    bool == (const Movie& movie){
            if (title == movie.title &&
                releaseDate.year == movie.releaseDate.year &&
                releaseDate.month == movie.releaseDate.month &&
                releaseDate.day == movie.releaseDate.day &&
                isPopular = movie.isPopular
            ){
        return true;
    }else{
        return false;
    }
    }

}; // Needs Semicolon


struct Customer {
    string name;
    int id;
    string email;
};


int main(){

    vector<Movie> movies;

    // Movie movie; // Don't use same name

    // Movie movie = {"Terminator", 1984}; // Has to be in order if doing it this way. 
        // The last part can be left out and that will be auto intialized then if it was intialized in the structure
    
    // movie.title = "Terminator"; 
    // movie.releaseYear = 5;

    // movies.push_back(movie);
    movies.push_back({"Terminator", {1984, 6, 1}});
    movies.push_back({"Terminator 2", 1987});

    Movie movie1 = {"Terminator", {1984, 6, 1}};
    Movie movie2 = {"Terminator 2", 1987};

    // auto [title, releaseYear, isPopular] {movie} // Dont have to set up each indiviual one each time.

    for (auto movie: movies){
        auto [title, releaseDate, isPopular] {movie};
        cout << "Movie Title: " << title << endl;
        cout << "Movie Release Year: " << releaseDate.year << endl;
        cout << "Movie Release Month: " << releaseDate.month << endl;
        cout << "Movie Release Day: " << releaseDate.day << endl;
        cout << "Movie Popular: " << isPopular << endl;
    }


    // You can compare properties but not the whole object itself
    // if (movie1.title == movie2.title){
    //     cout << "Equal\n";
    // }else{
    //     cout << "Not Equal\n";
    // }
    
    cout << movie1 == movie2 << endl;


    // cout << "Movie Title: " << movie.title << endl;
    // cout << "Movie Release Year: " << movie.releaseYear << endl;
    // cout << "Movie Popular: " << movie.isPopular << endl;


    Customer person;
    person.name = "Bob";
    person.id = 546;
    person.email = "bob@email.com";

    cout << "\nName: " << person.name << endl;
    cout << "ID: " << person.id << endl;
    cout << "Email: " << person.email << endl;

    return 0;
}




//  NOTES QUESTIONS

// What are structures?
    // A custom, abstract data type (adt) and a general model of something.

// How do you build a structure?
    // Seen Above

    // struct Customer {
    //     string name;
    //     int id;
    //     string email;
    // };

// What can be held in a structure?
    // variables of different data types, even other structure objects

// How do you access the information in a structure?
    // Seen Above
    // Using object_name.property_name
    // Using auto

// How do you overload an operator?
    // 
