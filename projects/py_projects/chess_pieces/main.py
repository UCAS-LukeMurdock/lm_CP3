# LM  Chess Pieces Project
from classes import *

def pause():
    input("\nPress Enter to continue...\n")

# def play(chess_game):
#     start = input("Enter in the position of the piece you want to move: ")
#     end = input("Enter in the position you want it to move to: ")
#     # translate letter into number positions:

#     # if len(start) != 2 or len(end) != 2:
#     #     print("Invalid input format. Please use the format 'A2'.")
#     #     return False
#     # start_col = ord(start[0].upper()) - ord('A') + 1
#     # start_row = int(start[1])
#     # end_col = ord(end[0].upper()) - ord('A') + 1
#     # end_row = int(end[1])
#     # start_pos = Position(start_col, start_row)
#     # end_pos = Position(end_col, end_row)
#     # piece = chess_game.getPieceAt(start_pos)
#     # if piece is None:
#     #     print(f"No piece found at {start_pos}.")
#     #     return False
#     try:
#         start_pos = Position(start)
#     chess_game.movePiece(piece, end_pos)

    


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

    
    print("\n\n***Start of Game Simulation***\n\n")

    print(chess_game)
    pause()
    print(chess_game.getAllPieces())
    pause()
    print(chess_game.getBoard())

    pause()
    
    print("\n***Some Pieces Move***\n")

    # Moving Pieces
    chess_game.movePiece(chess_game.whitePieces[8], Position(1,3)) # wPawn1 a2 to a3
    chess_game.movePiece(chess_game.blackPieces[9], Position(2,6)) # bPawn2 b7 to b6
    pause()
    chess_game.movePiece(chess_game.whitePieces[15], Position(8,3)) # wPawn8 h2 to h3
    chess_game.movePiece(chess_game.blackPieces[14], Position(7,6)) # Pawn7 g7 to g6
    chess_game.movePiece(chess_game.blackPieces[14], Position(7,6)) # bPawn7 g7 to g6 (invalid)
    pause()
    chess_game.movePiece(chess_game.whitePieces[14], Position(7,3)) # wPawn7 g2 to g3

    chess_game.movePiece(chess_game.blackPieces[2], Position(3,6))  # bKnight1 b8 to c6
    pause()

    chess_game.movePiece(chess_game.whitePieces[5], Position(6,2))  # wBishop2 f1 to f2 (invalid)
    chess_game.movePiece(chess_game.whitePieces[5], Position(7,2))  # wBishop2 f1 to g2

    chess_game.movePiece(chess_game.blackPieces[6], Position(4,7))  # bQueen d8 to d7 (invalid)
    pause()
    chess_game.movePiece(chess_game.whitePieces[6], Position(4,2))  # wQueen d1 to d2 (invalid)

    chess_game.movePiece(chess_game.whitePieces[7], Position(6,1))  # wKing e1 to f1

    chess_game.movePiece(chess_game.blackPieces[3], Position(4,5))  # bKnight2 g8 to e7 (invalid)
    chess_game.movePiece(chess_game.blackPieces[3], Position(6,5))  # bKnight2 g8 to f6 
    pause()

    chess_game.movePiece(chess_game.whitePieces[6], Position(5,1))  # wQueen d1 to e1
    pause()

    # Capturing Moves
    chess_game.movePiece(chess_game.whitePieces[5], Position(3,6))  # wBishop2 g2 to c6 (capture bKnight1)
    pause()
    chess_game.movePiece(chess_game.blackPieces[1], Position(8,3))  # bRook2 h8 to h3 (capture wPawn8)
    pause()

    # chess_game.whitePieces[1].move(Position(3,3))  # wKnight1 b1 to c3
    # chess_game.blackPieces[8].move(Position(4,5))  # bPawn5 d7 to d5
    # chess_game.whitePieces[3].move(Position(4,3))  # wPawn4 d2 to d3
    # chess_game.blackPieces[5].move(Position(6,5))  # bBishop2 f8 to f5
    # chess_game.whitePieces[0].move(Position(1,4))  # wRook1 a1 to a4 (invalid: should print cannot move)
    # chess_game.whitePieces[0].move(Position(1,3))  # wRook1 a1 to a3 (valid)

    print(chess_game)
    print(chess_game.getPiecesLeft())
    pause()
    print(chess_game.getPiecesLeft("White") + "\n\n" + chess_game.getPiecesLeft("Black"))
    pause()
    print(chess_game.getAllPieces())
    pause()
    print("\n\n***End of Game Simulation***\n\n")
    # play(chess_game)

main()

# move vs canMoveTo ??????
# Fix it so it just shows testing or make it game


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