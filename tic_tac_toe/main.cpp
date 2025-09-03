// LM  Tic-Tac-Toe Game

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;


bool end_game = false;
bool u_win = false;
bool c_win = false;
bool tied_game = false;

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


void check(){ // Checks when the board has met an ending requirement

    // Ties
    bool spaces_filled = true;
    for(int i=0;i<board_length;i++){
        for (int j=0;j<size(board[i]);j++){
            if(board[i][j] != "X" and board[i][j] != "O"){
                spaces_filled = false;
            }
        }
    }
    if (spaces_filled == true){
        end_game = true;
        tied_game = true;
    }

    // X and O Rows
    for(int i=0;i<board_length;i++){
        if (board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X"){
            end_game = true;
            u_win = true;
        }
        if (board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O"){
            end_game = true;
            c_win = true;
        }
    }
    // X and O Columns
    for(int j=0; j<3; j++){ // 0, 1, 2
        if (board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X"){
            end_game = true;
            u_win = true;
        }
        if (board[0][j] == "O" and board[1][j] == "O" and board[2][j] == "O"){
            end_game = true;
            c_win = true;
        }
    }
    // X and O Diagonals
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X"    or    board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"){
        end_game = true;
        u_win = true;
    }
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O"    or    board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"){
        end_game = true;
        c_win = true;
    }
}


void display(){ // Displays current status of game board
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


void user_turn(){ // The user gets to choose which empty space to put their X on
    bool x_placed = false;
    while (x_placed == false) {
        cout << "(Enter 0 to forfeit the game)\nWhere do you want to place X?:\n";
        string u_choice;
        cin >> u_choice;

        if(u_choice == "0"){
            end_game = true;
            break;
        }
        
        for(int i=0;i<board_length;i++){
            for (int j=0;j<size(board[i]);j++){
                if(board[i][j] == u_choice){
                    board[i][j] = "X";
                    x_placed = true;
                }
            }
        }
        if (x_placed == false)
            cout << "\nInvalid Spot Number\n\n";
    }
}


void comp_turn(){ // The Computer randomly places an O on an empty space
    bool correct_spot = false;
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
}


void play_game(){ // Sets up a Tic Tac Toe game and lets the user and computer take turns, displaying the board in between
    u_win = false;
    c_win = false;
    tied_game = false;
    end_game = false;
    board[0][0] = "1"; board[0][1] = "2"; board[0][2] = "3";
    board[1][0] = "4"; board[1][1] = "5"; board[1][2] = "6";
    board[2][0] = "7"; board[2][1] = "8"; board[2][2] = "9";

    while (true) {
        display();
        check();
        if (end_game == true){
            break;
        }

        user_turn();
        cout << "\nYour Turn:\n";

        display();
        check();
        if (end_game == true)
            break;
        
        comp_turn();
        cout << "\nComputer's Turn:\n";
    }
    if (u_win == true){
        cout << "You Won!\n";
    }else if (c_win == true){
        cout << "You Lost!\n";
    }else if (tied_game == true){
        cout << "Draw!\n";
    }else
        cout << "You Forfeited!\n";
}


int main(){ // Lets the user play Tic Tac Toe as many times as they like
    cout << "\n\nWelcome to Tic-Tac-Toe! In this game you will play against a computer by deciding which space (number) to place your X's.\n(The computer is slower as the board gets filled.)\n";
    while (true) {
        cout << "\nPlay Tic-Tac-Toe(1)  Exit(2)\nChoice: ";
        string play;
        cin >> play;

        if (play == "2"){
            cout << "\nCome back soon!\n\n";
            break;
        } else if (play == "1"){
            play_game();
        }else
        cout << "\nIncorrect Input\n";
    }
    return 0;
}