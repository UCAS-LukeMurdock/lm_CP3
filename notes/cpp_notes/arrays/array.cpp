// LM  Arrays Notes
#include <iostream>
#include <limits>
// #include <algorithm>
using namespace std;

string fam[12] = {"Mark", "Jennifer", "Kaylee", "Lori", "David", "Rachel", "Michael", "John", "Kristi", "Matthew", "Luke", "Cambree"};
string sibs[10] = {"Kaylee", "Lori", "David", "Rachel", "Michael", "John", "Kristi", "Matthew", "Luke", "Cambree"};

// array as an argument in a function
int search(string list[], size_t len, string item){
    // if(find(list->begin(), list->end(), item) != list->end()){
    //     cout << "You are a sibling\n!";
    // }
    for(int i=0; i < len; i++){
        if (list[i] == item){
            cout << "You are a sibling!\n";
            return 1;
        }
    }
    cout << "You are a parent!\n";
    return 0;
}

int main(){
    // cout << fam << endl;
    for(int i=0;i < size(fam);i++){
        cout << fam[i] << " Murdock\n";
        search(sibs, size(sibs), fam[i]);
        // if (fam[i] == sibs[i-2])
        //     cout << "They are a sibling!\n";
    }

    


// How are for loops constructed in C++?
    // for(Variable;Conditional;Changing Variable)
    // Ex: for(int i=0;i < size(fam);i++)

// When do you need to use curly brackets in C++?
    // If a code block takes up more than 1 line

// How do you compare items in arrays?
    // You can't compare the variable names themselves because that compares the location stored, use looping and indexing instead.

// How do you use an array as an argument in a function?
    // Seen Above

// What is type_t?
    // Type of T is a data type that is used to represent the size of objects (other data types).
    // Size of T is a placeholder that is used when we need to know how much space we have or we dont know how much space it takes up
    // type_t has the most storage capacity

    // SIZE OF T
    cout << numeric_limits<long long>::min() << endl;
    cout << numeric_limits<long long>::max() << endl;
    cout << numeric_limits<size_t>::min() << endl;
    cout << numeric_limits<size_t>::max() << endl;

// Why would we use type_t?
    // type_t can be used in place of another data type when declaring a variable
    // And Above Answer

// How do you search an array?
    // Seen Above (using a function and for loops)

// How do you sort an array?
    // Bubble sort takes two numbers and compares them to see if the first one is bigger and then switches them if that is the case.
    // It overlaps the pairs
    // It does the sort multiple times (iterations)
    // The number of changes ius equal to the number of items?

    int nums[] = {8,6,2,9,1,11};
    int length = size(nums);

    for(int j=0; j < length; j++){
        for(int i=1; i < length; i++){
            // cout << nums[i]<< endl;
            if (nums[i] < nums[i-1]){
                int swap = nums[i];
                nums[i] = nums[i-1];
                nums[i-1] = swap;
            }
        }
    }
    for(int i=0; i< length; i++)
        cout << nums[i] << ", ";
    cout << endl;
        

// How do you make a multi-dimensional array?
    // They are called matrices
    // You shouldn't go past 3d
    // matrix[rows][columns]
    int matrix[3][3] = {{1,2,3},
                        {4,5,6},
                        {7,8,9},};



    // Structured Binding (Packing)
    auto [q,w,e,r,t,y,u,i,o,p,a,s] = fam;
    cout << e << endl;


    return 0;
}