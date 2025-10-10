// LM  Strings, Arrays, Conditionals Notes
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    // low level version of random numbers
    int seconds = time(nullptr);
    srand(seconds);
    int my_num = rand() % 11;
    cout << my_num << endl;

    // Arrays need the index numbers listed in brackets when the variable is set
    int grades[11] = {99,24,48,67,48,84,77,85,68,98,9};
    cout << grades[3] << endl;

    // Strings
    char name[5] = "Luke";  // [5] = length + 1
    cout << name << endl;
    string sentence = "The quick brown fox jumps over the lazy dog"; // Remember ;
    cout << sentence << endl;
    cout << sentence.length() << endl;
    cout << (name > sentence) << endl; // Checks alphabetically
    // .starts_with("T") 
    // .ends_with()
    // .empty() 
    // .front() <- returns the first character
    // .back() <- returns the last character

    sentence.append(" LaRose");
    sentence.insert(7, "K ");
    // sentence.erase();
    // sentence.clear(); // Makes the string empty
    int first = sentence.find("fox"); // <- beginning index of 1st occurance
    int end = first + 3;
    sentence.replace(first, end, "badger");
    cout << sentence << endl;

    // Searching a string
    cout << sentence.find("Vienna") << endl;
    // rfind() <- starts the search at the end of the string (last occurance)
    // find_first_of() <- gets first occurance of any character in the given string
    cout << sentence.find("a") << endl; // .find() = .find_first_of()
    cout << sentence.find_first_of("a") << endl;
    // find_last_of()
    cout << sentence.find_first_not_of("The q") << endl;
    // .find_last_not_of()

    cout << sentence.substr(5,4) << endl; // .substr(Starting Index, Length it goes out)

    // Conditionals
    if (name.front() == sentence.front()){
        cout << name.front() << " is the same as " << sentence.front() << endl;
    }else if (name > sentence){
        cout << name.front() << " is later in the alphabet than " << sentence.front() << endl;
    }else{
        cout << name.front() << " is earlier in the alphabet than " << sentence.front() << endl;
    }

    return 0;
}


// What is Narrowing?
    // Moving information from a bigger variable to a smaller one.
    // You might lose information because it can't fit.

// What is a basic way to generate random numbers in C++?
    // Answer is Above (Seeding rand with time)

// What is an array?
    // A list of variables of the same data type

// How do I create an array?
    // Answer is Above (Arrays need the index numbers listed in brackets when the variable is set)

// How do you make strings in C?
    // char name[#] = "Characters"
    // Ex: char name[5] = "Luke";

// How did C++ improve creating strings? 
    // C++ made a new class for it in the standard library to make it simpler.
    // Ex: string sentence = "The quick brown fox jumps over the lazy dog";

// How do I search a string?
    // Using these methods:
    // cout << sentence.find("Vienna") << endl;
    // rfind() <- starts the search at the end of the string (last occurance)
    // find_first_of() <- gets first occurance of any character in the given string
    // cout << sentence.find("a") << endl; // .find() = .find_first_of()
    // cout << sentence.find_first_of("a") << endl;
    // find_last_of()
    // cout << sentence.find_first_not_of("The q") << endl;
    // .find_last_not_of()
    

// How do I modify a string?
    // Using these methods:
    // .append()
    // sentence.insert(7, "K ");
    // sentence.erase();
    // sentence.clear(); // Makes the string empty
    // sentence.replace(first, end, "badger");

// What are some string methods? 
    // .length()

    // .starts_with("T") .ends_with()
    // .empty() 
    // .front() <- returns the first character
    // .back() <- returns the last character

    // .append()
    // sentence.insert(7, "K ");
    // sentence.erase();
    // sentence.clear(); // Makes the string empty
    // sentence.replace(first, end, "badger");

    // cout << sentence.find("Vienna") << endl;
    // rfind() <- starts the search at the end of the string (last occurance)
    // find_first_of() <- gets first occurance of any character in the given string
    // cout << sentence.find("a") << endl; // .find() = .find_first_of()
    // cout << sentence.find_first_of("a") << endl;
    // find_last_of()
    // cout << sentence.find_first_not_of("The q") << endl;
    // .find_last_not_of()
