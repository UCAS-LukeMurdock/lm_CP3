// LM  Fahrenheit to Celsius

#include <iostream>
using namespace std;

int main(){
    cout << "This program converts Fahrenheit to Celsius."<<endl;
    cout << "What is your temperature in degrees Fahrenheit?: ";
    double num;
    cin >> num;
    double final_num = (num-32)*5/9;
    cout << num << " degrees in Fahrenheit is the same as " << final_num << " degrees in Celsius.";
    return 0;
}