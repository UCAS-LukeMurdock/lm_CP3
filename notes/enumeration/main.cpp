// LM  {} Notes

#include <iostream>
// #include <string>
// #include <memory>

using namespace std;

enum Action{ // It causes errors to use another enumerator that has the same name as a previous one. 
    List = 1, // Adds one as it goes on automatically when not intialized.
    Add,
    Update
};

// Strongly Typed Enumerator - You can't create two of the same of these.
enum class Operation{
    List = 1,
    Add,
    Update
};


void play(){
    cout << "\n";
}


int main(){
    int input;

    cout <<
    "1: List invoices" << endl <<
    "2: Add invoices" << endl <<
    "3: Update invoices" << endl <<
    "Select: ";
    cin >> input;

    // Switches
    switch(input){
        case Action::List:
            cout << "List invoices" << endl;
            break;
        case Action::Add:
            cout << "I haven't built this yet" << endl;
            break;
        case Action::Update:
            cout << "Suprisingly I haven't built this either" << endl;
            break;
    }



    if (input == static_cast<int>(Operation::List)){ // You have to specify the data type
        cout << "List invoices" << endl;
    }else if(input == Action::Add){
        cout << "I haven't built this yet" << endl;
    }else if(input == Action::Update){
        cout << "Suprisingly I haven't built this either" << endl;
    }else{
        cout << "Womp womp. Not an option." << endl;
    }

    return 0;
}


//  NOTES QUESTIONS

// What is enumeration?
    // A better way to make a menu with input options.
    // Has multiple constants at once.

// How do you build enumeration?
    // Seen Above

// How do we display our enumerator? 
    // Example:
    // cout <<
    // "1: List invoices" << endl <<
    // "2: Add invoices" << endl <<
    // "3: Update invoices" << endl <<
    // "Select: ";

// Why does it matter that enumerators are constants??
    // The constants are important because it makes it so it doesn't change accidentally.

// What is the default beginning enumerator? 
    // It starts at 0 and then increases by one.

// How do you give a different default value?
    // You intialize the first value.
    // Example: List = 1    (Seen Above)

// What is a strongly typed enumerator?
    // A strongly typed enumerator is an enumerator with something like "enum class Operation{}".

// How are strongly typed enumerators different from a normal one?
    // The differences are that you have to specify the data type and can't have two that have the same name when using a strongly typed enumerator, unlike normal ones.
