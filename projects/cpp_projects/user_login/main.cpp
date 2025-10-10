// LM  User Login

#include <iostream>
using namespace std;

string admin[3] = {"Luke", "Ms.LaRose", "Admin"};
string returning_user[5] = {"Nick", "Darius", "Matt", "Alex", "John"};

int main(){
    cout << "\n\nThis is a user login program." << endl;
    cout << "What is your name?: ";
    string name;
    cin >> name;

    if (name == admin[0]) {
        cout << "\nHello, Admin " << name;
    }else if (name == admin[1]) {
        cout << "\nHello, Admin " << name;
    }else if (name == admin[2]) {
        cout << "\nHello, Admin " << name;
    }else if (name == returning_user[0]) {
        cout << "\nWelcome back, " << name;
    }else if (name == returning_user[1]) {
        cout << "\nWelcome back, " << name;
    }else if (name == returning_user[2]) {
        cout << "\nWelcome back, " << name;
    }else if (name == returning_user[3]) {
        cout << "\nWelcome back, " << name;
    }else if (name == returning_user[4]) {
        cout << "\nWelcome back, " << name;
    }else {
        cout << "\nGreetings newcomer, " << name;
    }
    
    return 0;
}