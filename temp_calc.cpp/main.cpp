// LM  Fahrenheit to Celsius

#include <iostream>
using namespace std;

int main(){
    cout << "This program converts Fahrenheit to Celsius.";
    cout << "What is your temperature in degrees Fahrenheit?: ";
    float num;
    cin >> num;
    float final_num = (num-32)*5/9;
    cout << num << " degrees in Fahrenheit is the same as " << final_num << " degrees in Celsius.";
    return 0;
}
