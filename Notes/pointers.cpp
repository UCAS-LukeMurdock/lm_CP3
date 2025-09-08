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

int capacity = 5;
int* sanity = new int[capacity];
int entries = 0;


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
    cout << "\nComparing Pointers:\n" << (pnum == pday) << endl;
    cout << (pnum < pday) << endl;
    cout << (pnum > pday) << endl;
    if(pnum != nullptr){
        cout << *pnum << endl;
        pnum++; // It points somewhere else that is empty now.
    }
    cout << *pnum << endl; // It is empty so it prints something random.


    while(true){
        cout << "Number: ";
        cin >> sanity[entries];
        if(cin.fail()) break;
        entries++;
        if(entries == capacity){
            capacity += 5;
            int* temp = new int[capacity];
            for(int i = 0; i < entries; i++)
                temp[i] = sanity[i];
            delete[] sanity;
            sanity = temp;
        }
    }
    
    for (int i=0; i < entries; i++)
        cout << sanity[i] << endl;

    delete[] sanity;
    // delete[] sanity // Don't delete twice



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
    // You compare pointers by using the normal condition symbols and it will compare if they point at the same location or if it is at a further on location or a closer one.

// What is dynamic memory allocation?
    // Changing the storage amount and places of an array.

// What is the Stack?
    // An area of memory used for managing funciton calls, local variables, and control flow. It is managed by the compiler for quick allocation of memory.

// What is the Heap?
    // An area of memory used for dynamic memory. Stores data if the size is unknown at the time of compiling. Memory must be manually managed by the program. Used for flexible long-lived storage of complex data structures, objects, and large files.

// What are smart pointers?
    // On Smart Pointers File
    // Smart pointers are variables that work on the stack instead of the heap.
    // They delete themselves after they aren't neeeded.

    // Unique pointers owns that piece of the memory, nothing else can use it.
    // Shared pointers allow it so multiple pointers can point at that same place.
    

    cout << "\n\n";

    return 0;
}