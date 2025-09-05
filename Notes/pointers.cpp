// LM  Pointers Notes

#include <iostream>
using namespace std;


int numbers[] = {4, 2, 6, 8, 14, 24, 65};

void divide(int* list, int size){ // Arrays need size
    cout << "\nThe numbers list is: " << *list << endl;
    for(int i; i < size; i++){
        list[i] = list[i]/2;
        cout << list[i] << endl;
    }
}


int main(){
    cout << "\n\n";

    int num = 4;
        // & is for address, * is for computer knowing it is a pointer, the p is for humans to know it is a pointer
    int* pnum = &num;
    int day = 5;
    int month = 9;
    

    // Constants are variables that you can't change the value of
    const double pi = 3.141592;
    const double gpa = 3.99999;

    *pnum = 8; // Changes the value in the pointer's location
    // pi = 89.3;  // Error: changing a constant


    // Constant pointers
    const double* ppi = &pi; // The value at the location cannot be changed.    The pointer is stuck on that data type also
    ppi = &gpa; // You can switch where the pointer points (change its address)

    int* const pday = &day; // can change value, but not location being pointed at
    *pday = 6;
    // *pday = &num; // Error: You can't change where the pointer is pointing at (You can't change the address)

    const int* const pmonth = &month; // Location and value cannot change


    cout << "The number: " << num << endl;
    cout << "The location of num: " << pnum << endl;
    cout << "The value of the location of num: " << *pnum << endl;

    divide(numbers, size(numbers));


// What is a pointer?
    // Pointers hold addresses instead of the information you would assume/want.
    // Arrays automatically use pointers

// Why do we use pointers?
    // We use it so the copmuter doesnt have to waste space on copying/moving the location and instead can just go to where it already is
    // Analogy: It is easier to tell people where the free pizza is instead of bringing the pizza there

// How do I create a pointer?
    // Ex: int* pnum = &num;

// What is indirection or de-referencing?
    // It is getting the value of the location in the pointer instead of the address
    // Ex: *pnum

// What are constant pointers? How are the different types used?
    // They are pointers with different parts that can't be changed

// How do you pass a pointer into a function?
    // Look Above
    // The Example:
    // int numbers[] = {4, 2, 6, 8, 14, 24, 65};

    // void divide(int* list, int size){ // Arrays need size
    //     cout << "\nThe numbers list is: " << *list << endl;
    // }

    // divide(numbers, size(numbers));

// Why would you pass a pointer to a function?
    // You would pass a pointer into a function because you don't want to actually give it a lot of info, you just want to tell it where to find the information.

// How do you compare pointers?
    // 

// What is dynamic memory allocation?
    // 

// What is the Stack?
    // 

// What is the Heap?
    // 

// What are smart pointers?
    // 
    

    cout << "\n\n";

    return 0;
}