// LM Test





// LM  Tic-Tac-Toe Game

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;


bool end_game = false;
bool u_win = false;
bool c_win = false;
bool tied_game = false;
string shownBoard = "";

string board[3][3] = {{"1", "2" ,"3"},
                    {"4", "5" ,"6"},
                    {"7", "8" ,"9"}};

int board_length = size(board);

/*
_1_|_2_|_3_
_1_|_2_|_3_
 1 | 2 | 3 
*/

// j is columns and i is rows


void check(string board[3][3]){

    // Ties
    tied_game = true;
    end_game = true;

    for(int i=0;i<board_length;i++){
        for (int j=0;j<size(board[i]);j++){
            if(board[i][j] != "X" and board[i][j] != "O"){
                tied_game = false;
                end_game = false;
            }
        }
    }

    // X Rows
    for(int i=0;i<board_length;i++){
        if (board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X"){
            end_game = true;
            u_win = true;
        }
    }
    // X Columns
    for(int j=0; j<3; j++){ // 0, 1, 2
        if (board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X"){
            end_game = true;
            u_win = true;
        }
    }
    // X Diagonal
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"    or    board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"){
        end_game = true;
        u_win = true;
    }

    // O Rows
    for(int i=0;i<board_length;i++){
        if (board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O"){
            end_game = true;
            c_win = true;
        }
    }
    // O Columns
    for(int j=0; j<3; j++){ // 0, 1, 2
        if (board[0][j] == "O" and board[1][j] == "O" and board[2][j] == "O"){
            end_game = true;
            c_win = true;
        }
    }
    // O Diagonal
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"    or    board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"){
        end_game = true;
        c_win = true;
    }
}

void display(string board[3][3]){
    string board_display = "";

    for(int i=0;i<board_length;i++){
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
}

int main(){
    cout << "\n\nWelcome to Tic-Tac-Toe! In this game you will play against a computer by deciding which space(number) to place your X's.\n";
    while (true) {
        cout << "\nPlay Tic-Tac-Toe(1)  Exit(2)\nChoice: ";
        string play;
        cin >> play;

        if (play == "2"){
            cout << "\nCome back soon!\n";
            break;

        } else if (play == "1"){
            u_win = false;
            c_win = false;
            tied_game = false;
            end_game = false;
            string board[3][3] = {{"1", "2" ,"3"}, {"4", "5" ,"6"}, {"7", "8" ,"9"}};

            while (true) {
                bool correct_spot = false;

                display(board);
                check(board);
                if (end_game == true){
                    break;
                }

                cout << "Where do you want to place X?:\n";
                string u_choice;
                cin >> u_choice;
                for(int i=0;i<board_length;i++){
                    for (int j=0;j<size(board[i]);j++){
                        if(board[i][j] == u_choice)
                            board[i][j] = "X";
                    }
                }
                cout << "\nYour Turn:\n";
                display(board);
                check(board);
                if (end_game == true)
                    break;
                
                while (correct_spot == false){
                    int seconds = time(nullptr);
                    srand(seconds);
                    int c_choice = (rand() % 10) +1;
                    
                    for(int i=0;i<board_length;i++){
                        for (int j=0;j<size(board[i]);j++){
                            if(board[i][j] == to_string(c_choice)){
                                board[i][j] = "O";
                                correct_spot = true;
                            }    
                        }
                    }
                }
                cout << "\nComputer's Turn:\n";
            }
            if (u_win == true){
                cout << "You Won!\n";
            }else if (c_win == true){
                cout << "You Lost!\n";
            }else if (tied_game == true){
                cout << "Draw!\n";
            }
            
        }else
        cout << "\nIncorrect Input\n";
    }
    return 0;
}

// Fix winning

// ask her why the board isnt globalized
// Is it fine that it doesn't let the player have a second chance when picking where to place X








// #include <iostream>
// using namespace std;

// // 🔹 Global board
// string board[3][3] = {
//     {"1", "2", "3"},
//     {"4", "5", "6"},
//     {"7", "8", "9"}
// };

// void display() {
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             cout << board[i][j] << " ";
//         }
//         cout << endl;
//     }
// }

// void update_board() {
//     board[0][0] = "X"; // Just change the top-left cell
// }

// int main() {
//     cout << "Before update:\n";
//     display();         // Should show 1 2 3 ... etc.

//     update_board();    // Changes board[0][0] = "X"

//     cout << "\nAfter update:\n";
//     display();         // ✅ Should show X 2 3 ... etc.

//     return 0;
// }
