// LM  Dynamic Array

#include <iostream>
#include <string>
#include <memory>

using namespace std;


int main(){

    cout << "\n\nWelcome to this List of Colors Program, where you can enter in as many colors as you want.\n";
    while()

        int capacity = 5;
        // auto string_array_ptr = std::make_shared<std::string[]>(array_size);
        shared_ptr <string[]> inputs(new string[capacity]);
        int entries = 0;

        cout << "[Enter 0 to Stop]" << endl;
        while(true){
            cout << "Enter a Color: ";
            string input;
            getline(cin, input);
            if(input == "0")
                break;

            inputs[entries] = input;
            if(cin.fail()) break;
            entries++;


            if(entries == capacity){
                capacity += 5;
                shared_ptr <string[]> temp(new string[capacity]);

                for(int i = 0; i < entries; i++)
                    temp[i] = inputs[i];

                inputs.reset();
                inputs = temp;
            }
        }

        for (int i=0; i < entries; i++)
            cout << inputs[i] << ", ";

    cout << "\n\n\nCome Back Soon!\n\n\n" << endl;

    return 0;
}