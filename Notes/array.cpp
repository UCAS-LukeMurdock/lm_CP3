// LM  Arrays Notes
#include <iostream>
using namespace std;

string fam[12] = {"Mark", "Jennifer", "Kaylee", "Lori", "David", "Rachel", "Michael", "John", "Kristi", "Matthew", "Luke", "Cambree"};
string sibs[10] = {"Kaylee", "Lori", "David", "Rachel", "Michael", "John", "Kristi", "Matthew", "Luke", "Cambree"};

void search(string list, string item){
    cout << list << endl;
}

int main(){
    for(int i=0;i < size(fam);i++){
        cout << fam[i] << " Murdock\n";
        if (fam[i] == sibs[i-2])
            cout << "They are a sibling!\n";
    }

    return 0;
}


// How are for loops constructed in C++?
    // Ex: for(int i=0;i < size(fam);i++)

// When do you need to use curly brackets in C++?
    // If a code block takes up more than 1 line

// How do you compare items in arrays?
    // You can't compare the variable names themselves because that compares the location stored, use looping and indexing.

// How do you use an array as an argument in a function?
    // 

// What is type_t?
    // 

// Why would we use type_t?
    // 

// How do you search an array?
    // 

// How do you sort an array?
    // 

// How do you make a multi-dimensional array?
    // 
