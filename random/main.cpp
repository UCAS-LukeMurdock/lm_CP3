// LM Test

#include <iostream>
using namespace std;

// 🔹 Global board
string board[3][3] = {
    {"1", "2", "3"},
    {"4", "5", "6"},
    {"7", "8", "9"}
};

void display() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

void update_board() {
    board[0][0] = "X"; // Just change the top-left cell
}

int main() {
    cout << "Before update:\n";
    display();         // Should show 1 2 3 ... etc.

    update_board();    // Changes board[0][0] = "X"

    cout << "\nAfter update:\n";
    display();         // ✅ Should show X 2 3 ... etc.

    return 0;
}
