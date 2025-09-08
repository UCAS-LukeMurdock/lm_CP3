// LM  Smart Pointers

#include <iostream>
#include <memory>

using namespace std;


int main(){
// unique pointers
    // unique_ptr <int> y = make_unique<int>(); // A way that is long and you shouldn't use
    unique_ptr <int> x(new int);
    auto y = make_unique<int>(); // Another Way
    *x = 10;
    *y = 7;
    cout << *x << endl;

// shared pointers
    auto z = make_shared<int>();
    *z = 4;

    cout << *x << ", " << *y << ", " << *z << endl;

    return 0;
}