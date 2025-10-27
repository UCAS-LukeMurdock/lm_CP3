# LM  Chess Pieces Project
from classes import *

def pause():
    input("\nPress Enter to continue...\n")

def convert(user_pos):
    if user_pos[0] == 'A' or user_pos[0] == 'a':
        user_pos = f"1{user_pos[1]}"
    elif user_pos[0] == 'B' or user_pos[0] == 'b':
        user_pos = f"1{user_pos[2]}"
    elif user_pos[0] == 'C' or user_pos[0] == 'c':
        user_pos = f"1{user_pos[3]}"
    elif user_pos[0] == 'D' or user_pos[0] == 'd':
        user_pos = f"1{user_pos[4]}"
    elif user_pos[0] == 'E' or user_pos[0] == 'e':
        user_pos = f"1{user_pos[5]}"
    elif user_pos[0] == 'F' or user_pos[0] == 'f':
        user_pos = f"1{user_pos[6]}"
    elif user_pos[0] == 'G' or user_pos[0] == 'g':
        user_pos = f"1{user_pos[7]}"
    elif user_pos[0] == 'H' or user_pos[0] == 'h':
        user_pos = f"1{user_pos[8]}"
    return user_pos

def play(chess_game):
    start = input("\nEnter in the position of the piece you want to move: ").strip()
    end = input("\nEnter in the position you want it to move to: ").strip()

    try:
        start = convert(start)
        end = convert(end)
        start_pos = Position(int(start[0]), int(start[1]))
        piece = chess_game.getPieceAt(start_pos)
        if piece is None:
            print("\nNo piece found at your starting position!")
            return
        piece.move(Position(int(end[0]), int(end[1])), chess_game)
    except:
        print("\nInvalid Input (Please enter positions in format 'A2', 'E5', etc.)")


    


def main(): # Creates Objects 

    chess_game = ChessGame()

    # Black Pieces
    chess_game.blackPieces.append(Rook("Black", Position(1,8), name="Rook 1"))
    chess_game.blackPieces.append(Rook("Black", Position(8,8), name="Rook 2"))

    chess_game.blackPieces.append(Knight("Black", Position(2,8), name="Knight 1"))
    chess_game.blackPieces.append(Knight("Black", Position(7,8), name="Knight 2"))

    chess_game.blackPieces.append(Bishop("Black", Position(3,8), name="Bishop 1"))
    chess_game.blackPieces.append(Bishop("Black", Position(6,8), name="Bishop 2"))

    chess_game.blackPieces.append(Queen("Black", Position(4,8), name="Queen"))
    chess_game.blackPieces.append(King("Black", Position(5,8), name="King"))

    chess_game.blackPieces.append(Pawn("Black", Position(1,7), name="Pawn 1"))
    chess_game.blackPieces.append(Pawn("Black", Position(2,7), name="Pawn 2"))
    chess_game.blackPieces.append(Pawn("Black", Position(3,7), name="Pawn 3"))
    chess_game.blackPieces.append(Pawn("Black", Position(4,7), name="Pawn 4"))
    chess_game.blackPieces.append(Pawn("Black", Position(5,7), name="Pawn 5"))
    chess_game.blackPieces.append(Pawn("Black", Position(6,7), name="Pawn 6"))
    chess_game.blackPieces.append(Pawn("Black", Position(7,7), name="Pawn 7"))
    chess_game.blackPieces.append(Pawn("Black", Position(8,7), name="Pawn 8"))

    # White Pieces
    chess_game.whitePieces.append(Rook("White", Position(1,1), name="Rook 1"))
    chess_game.whitePieces.append(Rook("White", Position(8,1), name="Rook 2"))

    chess_game.whitePieces.append(Knight("White", Position(2,1), name="Knight 1"))
    chess_game.whitePieces.append(Knight("White", Position(7,1), name="Knight 2"))

    chess_game.whitePieces.append(Bishop("White", Position(3,1), name="Bishop 1"))
    chess_game.whitePieces.append(Bishop("White", Position(6,1), name="Bishop 2"))

    chess_game.whitePieces.append(Queen("White", Position(4,1), name="Queen"))
    chess_game.whitePieces.append(King("White", Position(5,1), name="King"))

    chess_game.whitePieces.append(Pawn("White", Position(1,2), name="Pawn 1"))
    chess_game.whitePieces.append(Pawn("White", Position(2,2), name="Pawn 2"))
    chess_game.whitePieces.append(Pawn("White", Position(3,2), name="Pawn 3"))
    chess_game.whitePieces.append(Pawn("White", Position(4,2), name="Pawn 4"))
    chess_game.whitePieces.append(Pawn("White", Position(5,2), name="Pawn 5"))
    chess_game.whitePieces.append(Pawn("White", Position(6,2), name="Pawn 6"))
    chess_game.whitePieces.append(Pawn("White", Position(7,2), name="Pawn 7"))
    chess_game.whitePieces.append(Pawn("White", Position(8,2), name="Pawn 8"))

    
    print("\n\n***Start of Game Simulation***\n")

    print(chess_game)
    pause()
    print(chess_game.getAllPieces())
    pause()
    print(chess_game.getBoard())

    pause()

    while True:
        choice = input("\nDo you want to move a piece? (Y/N): ").strip().upper()
        if choice == 'N':
            break
        elif choice == 'Y':
            play(chess_game)
        else:
            print("\nInvalid Input (Please enter 'Y' or 'N')")

    print(chess_game)
    print(chess_game.getPiecesLeft())
    pause()
    print(chess_game.getPiecesLeft("White") + "\n\n" + chess_game.getPiecesLeft("Black"))
    pause()
    print(chess_game.getAllPieces())
    pause()
    print(chess_game.getBoard())
    print("\n\n***End of Game Simulation***\n\n")

main()


"""
INSTRUCTIONS:
    Create the base classes needed to build a chess game
    (Note: you are not building chess all the way to the end!).
    Use the class diagram below to create your code!

    Once all of your classes are set up create the correct number of pieces for each player,
    set them up on the board,
    move 5 different pieces. 

EXAMPLE OUTPUT:
    White Knight 1, Symbol K  is at B1
    Black Pawn 5, Symbol P is at D7
    White Pawn 4, Symbol P is at D2
    Black Bishop 2, Symbol B is at C8
    White Rook 1, Symbol R is at A1

    ***After moves***

    White Knight 1, Symbol K  is at C3
    Black Pawn 5, Symbol P is at D5
    White Pawn 4, Symbol P is at D3
    Black Bishop 2, Symbol B is at F5
    White Rook 1 cannot move to A4

KEY REMINDERS:
    Follow the provided class diagram exactly 
    Implement ChessPiece as an abstract class 
    Create all six concrete piece classes (Pawn, Rook, Knight, Bishop, Queen, King) 
    Implement canMoveTo(), getSymbol(), setPosition(), and getColor() methods 
    Create ChessGame class with whitePieces and blackPieces lists 
    Implement movePiece(), removePiece(), getPiecesLeft(), and getPieceAt() in ChessGame 
    Create correct number of pieces for each player 
    Set up pieces in starting positions 
    Demonstrate moving 5 different pieces 
    Implement basic move validation for each piece type 
    Use removePiece() method for capturing 
    Put all classes on 1 file separate from your running file 
    Add comments to explain your code 
    Test each piece type for correct movement 
    Focus on core functionality over advanced game logic

RUBRIC:
    Class Structure
        5 pts
        Full Marks
    All classes (ChessPiece, Pawn, Rook, Knight, Bishop, Queen, King, ChessGame) are implemented correctly following the class diagram. ChessPiece is abstract.
        3 pts
        Partial Credit
    Most classes are implemented, but there are minor deviations from the class diagram or 1-2 classes are missing.
        0 pts
        No Marks
    Major deviations from the class diagram or more than 2 classes are missing.
        5 pts
    This criterion is linked to a Learning OutcomeMethod Implementation
        5 pts
        Full Marks
    All required methods (canMoveTo(), getSymbol(), movePiece(), removePiece(), getPiecesLeft(), getPieceAt()) are correctly implemented with basic functionality.
        3 pts
        Partial Credit
    Most methods are implemented, but 1-2 have incorrect or incomplete functionality.
        0 pts
        No Marks
    More than 2 methods are missing or have major errors in implementation.
        5 pts
    This criterion is linked to a Learning OutcomePiece Creation and Setup
        5 pts
        Full Marks
    Correct number of pieces created for each player and set up in proper starting positions on the board.
        3 pts
        Partial Credit
    Most pieces are created and set up correctly, but there are minor errors in quantity or positioning.
        0 pts
        No Marks
    Major errors in piece creation or setup, or this step is entirely missing.
        5 pts
    This criterion is linked to a Learning OutcomeMove Demonstration
        5 pts
        Full Marks
    5 different pieces are moved correctly, demonstrating proper use of movePiece() method and basic move validation.
        3 pts
        Partial Credit
    3-4 pieces are moved correctly, or all 5 are moved but with minor errors.
        0 pts
        No Marks
    Fewer than 3 pieces are moved, or moves are implemented incorrectly.
        5 pts
    This criterion is linked to a Learning OutcomeCode Organization and Comments
        5 pts
        Full Marks
    All classes are in one file separate from the running file. Code is well-organized and thoroughly commented to explain functionality.
        3 pts
        Partial Credit
    Classes are mostly organized correctly with some comments, but organization or commenting could be improved.
        0 pts
        No Marks
    Poor code organization, classes not separated correctly, or lack of meaningful comments.
"""