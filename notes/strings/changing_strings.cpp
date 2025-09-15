// LM  Changing Strings Notes

#include <iostream>
#include <string>
using namespace std;

string name = "vienna laRose";
string sentence = "The quick brown fox jumps over the lazy dog!";

int main(){
    auto index = name.find(' ');
    cout << "Index: " << index << endl;

    string first_name = name.substr(0,index);
    string last_name = name.substr(index+1); // without a second parameter then it goes to the end

    first_name[0] = toupper(first_name[0]);
    //tolower()

    cout << "First Name: " << first_name << endl;
    cout << "Last Name: " << last_name << endl;

    cout << "Sentence: " << sentence << endl;
    int length = size(sentence);
    for(int i=0; i<length; i++){
        if (isspace(sentence[i])){
            sentence[i] = '_';
        }else if(isupper(sentence[i])){
            sentence[i] = tolower(sentence[i]);
        }else{
            sentence[i] = char((int(sentence[i] ) +4) % 26 +97 );
        }
    }
    cout << "Changed Sentence: " << sentence << endl;
    
    cout << "This is a \"Question\"\n\t. . . I think" << endl; // escaping
    cout << R"(This is a "Question". . . I think)" << endl; // raw string

    return 0;
}

// How do I get a substring from within a string?
    // string.substr(starting_index, amount_of_chars)

// How do I create an escape character in C++?
    // You create an escape characte by using the backslash (\) and a specific character that does a specific thing.
    // Ex: \" \n \t

// How do I convert a string to another data type?
    // by using stoi() or stof() [s to type_name()]

// What is a raw string and when would I use it?
    // A raw string is a string that can be defined without needing to escape special characters.
