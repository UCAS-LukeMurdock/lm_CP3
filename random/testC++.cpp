// LM  Testing

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

string board[3][3] = {{"1", "2" ,"3"},
                    {"4", "5" ,"6"},
                    {"7", "8" ,"9"}};


int main(){


string board_display = "";

for(int i=0;i<size(board);i++){
    for(int j=0;j<size(board[i]);j++){
        if(i == 2){
            board_display.append(" " + board[i][j] + " |");
        }else {
            board_display.append("_" + board[i][j] + "_|");
        }
    }
    board_display[i*12 +11] = '\n'; // Replaces the unecessary | with a new line
}
cout << endl << board_display << endl;





    return 0;
}


/*

_1_|_2_|_3_
_1_|_2_|_3_
 1 | 2 | 3 

*/
