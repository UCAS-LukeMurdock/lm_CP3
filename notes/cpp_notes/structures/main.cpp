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

}; // Needs Semicolon

struct Customer {
    string name;
    int id;
    string email;
};


// Overloading ==   It is more clear when it is a function instead of a method.
bool operator==(const Movie& first, const Movie& second){
    return (first.title == second.title &&
        first.releaseDate.year == second.releaseDate.year &&
        first.releaseDate.month == second.releaseDate.month &&
        first.releaseDate.day == second.releaseDate.day &&
        first.isPopular == second.isPopular
    );
}

ostream& operator<<(ostream& stream, Movie& movie){
    stream << movie.title;
    return stream;
}

ostream& operator<<(ostream& stream, Customer& customer){
    stream << customer.name;
    return stream;
}


void showMovie(Movie* movie){
    cout << "Movie: " << movie->title << endl; // Pointer operator (->): used to acccess details of a structure pointer
}

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
    showMovie(&movie1);

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
    if(movie1 == movie2)
        cout << movie1 << " is equal to " << movie2 << endl;
    else{
        cout << movie1 << " is not " << movie2 << endl;
    }

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
    // struct name {
    //     property_type property_name;
    // };

    // Seen Above

    // Example:
        // struct Customer {
        //     string name;
        //     int id;
        //     string email;
        // };

// What can be held in a structure?
    // Structures hold variables of different data types, even other structure objects, and methods (functions)

// How do you access the information in a structure?
    // Seen Above
    // Using object_name.property_name
    // Using auto helps

// How do you overload an operator?
    // You add a function that overloads an operator such as == and makes it so it does the function's code instead of what it would usually do with that operator.
    // You have to do this becuase it doesn't know what to do with operator symbols on new data types you make.