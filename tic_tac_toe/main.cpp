// LM  Tic-Tac-Toe Game

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;


bool end = false;
bool winU = false;
bool winC = false;
bool tie = false;
string shownBoard = "";

string board[3][3] = {{"1", "2" ,"3"},{"4", "5" ,"6"},{"7", "8" ,"9"}};

// def check():
//     global end
//     global winU
//     global winC
//     global tie
//     columnCheck = [0, 1, 2]
//     columnX = 0

//     # Ties
//     tie = True
//     end = True
//     for row in board:
//         for space in row:
//             if space != "X" or space != "O":
//                 tie = False
//                 end = False

//     # X Rows
//     for row in board:
//         if row == ["X", "X", "X"]:
//             end = True
//             winU = True
//     # X Columns
//     for columnNum in columnCheck:
//         columnX = False
//         for row in board:
//             if row[columnNum] == "X":
//                 columnX += 1
//             if columnX == 3:
//                 end = True
//                 winU = True
//     # X Diagonal
//     if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
//         end = True
//         winU = True
//     if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
//         end = True
//         winU = True

//     # O Rows
//     for row in board:
//         if row == ["O", "O", "O"]:
//             end = True
//             winC = True
//     # O Columns
//     for columnNum in columnCheck:
//         for row in board:
//             columnX = False
//             if row[columnNum] == "O":
//                 columnX += 1
//             if columnX == 3:
//                 end = True
//                 winC = True
//     # O Diagonal
//     if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
//         end = True
//         winC = True
//     if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
//         end = True
//         winC = True

int display(string board){
    for (int i=0;i<)

        cout << row << endl;

        //check();
        return 0;
}


int main(){
    cout << "\n\nWelcome to Tic-Tac-Toe! In this game you will play against a computer by deciding which space(number) to place your X's." << endl;
    while (true) {
        cout << "(1)Play Tic-Tac-Toe  (2)Exit\nChoice: ";
        string play;
        cin >> play;
        if (play == "2")
            break;
        else if (play == "1"){
            while (true) {
                bool correct_spot = false

                // Move to back and make it not while true
                // for(row ?in board)

                display(board);
                
                if (end == true){
                    break;
                }
                    break;

                cout << "Where do you want to place X?:\n" << endl;
                string u_choice;
                cin >> u_choice;
                // for row_index, row in enumerate(board){
                    // for space_index, space in enumerate(row){
                        if (str(space) == u_choice)
                            board[row_index][space_index] = "X";
                    {
                }
                    
                for (row in board)
                    cout << row << endl;
                check();
                if (end == true)
                    break;

                while (correct_spot == false){
                    int seconds = time(nullptr);
                    srand(seconds);
                    int my_num = (rand() % 10) +1;

                    c_choice = r.randrange(1, 10)
                    for (row_index, row in enumerate(board)){
                        for (spaceIndex, space in enumerate(row)){
                            if (str(space) == str(choiceC)){
                                board[rowIndex][spaceIndex] = "O"
                                correctSpot = True
                            }
                                
                        }
                            
                    }
                        
                }
                cout << endl;
            }
            if (u_win == true)
                cout << "You Won!\n";
            else if (c_win == true)
                cout << "You Lost!\n";
            else if (tie == true)
                cout << "Draw!\n";

        }else
        cout << "Incorrect Input\n";
    }
    return 0;
}



// int search(string list[], size_t len, string item){
//     // if(find(list->begin(), list->end(), item) != list->end()){
//     //     cout << "You are a sibling\n!";
//     // }
//     for(int i=0; i < len; i++){
//         if (list[i] == item){
//             cout << "You are a sibling!\n";
//             return 1;
//         }
//     }
//     cout << "You are a parent!\n";
//     return 0;
// }

// int main(){
//     // cout << fam << endl;
//     for(int i=0;i < size(fam);i++){
//         cout << fam[i] << " Murdock\n";
//         search(sibs, size(sibs), fam[i]);
//         // if (fam[i] == sibs[i-2])
//         //     cout << "They are a sibling!\n";
//     }