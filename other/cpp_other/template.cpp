// LM  Program

#include <iostream> // Input and Output (i and o streams)
#include <limits>
#include <fstream> // read and write (if and of streams) [input and output]
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

/*

*/

// Enumeration for the menu options
enum Menu{
    First = 1,
    Second,
    Third,
    Fourth,
    Exit
};

// // Structure to hold a struct
// struct Struct{
//     // string name;
//     // int score;
//     // string date;
// };

// vector<Name> names; // Vector to hold the names


int getNumber(const string& prompt){ // Gets a valid integer from the user
    int num;
    while (true){
        cout << prompt;
        cin >> num;
        if(cin.fail()){
            cout << "\nInvalid Input\nEnter a valid number!\n";
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
            cout << "\nInvalid Input\nEnter a valid input!\n";
        }else break;
    }
    return str;
}


void read_file(){ // Reads the scores from the file into the vector
    ifstream ifile;
    ifile.open("file.csv");
    string line;

    if(ifile.is_open()){
        getline(ifile,line);

        while(getline(ifile,line)){
            istringstream iss(line);
            string item;

            Score temp_score;
            getline(iss, item, ',');
            temp_score.name = item;
            getline(iss, item, ',');
            temp_score.score = stoi(item);
            getline(iss, item, ',');
            temp_score.date = item;

            scores.push_back(temp_score);
        }
        ifile.close();
    }
}

void write_file(){ // Writes the scores from the vector into the file
    ofstream ofile;
    ofile.open("scores.csv");
    if(ofile.is_open()){
        ofile << "Name,Score,Date\n"; // Header
        for(const Score &s: scores){
            ofile << s.name << "," << s.score << "," << s.date << endl;
        }
        ofile.close();
    }
}


void play(){
    cout << "Hi\n";
}


int main(){ // This welcomes the user and lets the user choose to use or exit the program.
    cout << "\n\nWelcome to this Program, which...\n";
    while(true){

        int choice = getNumber(
            "\nMenu:\n"
            "(1) \n"
            "(2) \n"
            "(3) \n"
            "(4) \n"
            "(5) Exit\n"
            "Choice: ");

        if (choice == First){
            cout << "\nFirst option\n";
        }else if(choice == Second){
            cout << "\nSecond option\n";
        }else if(choice == Third){
            cout << "\nThird option\n";
        }else if(choice == Fourth){
            cout << "\nFourth option\n";
        }else if(choice == Exit){
            cout << "\n\n\nCome Back Soon!\n\n\n";
            break;
        }else{
            cout << "\nInvalid Input (Enter an Integer 1-5)\n";;
        }
    }
    return 0;
}





// LM  {} Notes

#include <iostream>
#include <string>

using namespace std;


void play(){
    cout << "\n";
}


int main(){

    cout << "\n";

    return 0;
}


// NOTES QUESTIONS
