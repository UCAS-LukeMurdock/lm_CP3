// LM  Basics Notes (Variables, Data Types, Inputs and Outputs Notes)

#include <iostream>
using namespace std;

main(){
    int students = 11;
    double days = 5;
    long years = 2554l; //long will compile to an int without l at the end
    const float pi = 3.14f; //float will compile to double without f at the end
    bool on = true;
    char name = 'V';
    cout << "Tell me your age: ";
    int age;
    cin >> age;
    cout << "You are "<< age<<endl;
    double divide = students/days; //If both variables are integers then division will not give a double/float. int can force it to stay int.
    cout << divide;
    return 0;
}

/*
How are static and dynamically typed variables different?
    Dynamically typed reads what type it is by itself.
    Statically needs you to tell it what it should be and it will make sure it is that value from then on.
    You have to say the type before the name.
        Ex: int name = value
    Best practice is for each variable to have its own line with its type and value declaration.
    
    Data Types:
    Type | Bytes | Possible values
    short | 2 | -32,768-32,768
    int | 4 | -2b to 2b
    long | same | same
    long long | 8 | big numbers
    floats | 4 | 3.4E38
    doubles | 8 | 1.7E308
    long double | 8 | 3.4E932
    bool | 1 | true/false
    char | 1 | single letter

REMINDER: What is the difference between instantiating and declaring a variable?
    Declaring is saying a variable exists.
    Instatiating is giving a variable a value, I think. Or creating an instance of a class.

What case type should be used for c++ variables?
    snake_case

What is the C++ standard library?
    The repository of all of the things that make it easier in C++ than C. It's like a python library.

How do you access the standard library?
    #include <library_name>

How do you create an output in C++?
    std::cout << "Number of students "<< students;

How do you create an input in C++?
    cout << "Tell me your age: ";
    int age;
    cin >> age;

What is the stream in C++?
    The stream is the flow of information, where it is going (in or out).

What is a constant?
    It makes it so you can't change the value of a variable.
    const type name;

Why do we write constants?
    It keeps the variables safe if you forget you don't want to change a certain varaible.

*/
