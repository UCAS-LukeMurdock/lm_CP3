# LM  Chess Pieces Project
from classes import *

# board = [ ["r","n","b","q","k","b","n","r"],
#         ["p","p","p","p","p","p","p","p"],
#         [" "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "],
#         [" "," "," "," "," "," "," "," "],
#         ["P","P","P","P","P","P","P","P"],
#         ["R","N","B","Q","K","B","N","R"] ]

def main(): # Creates Objects 

    chess_game = ChessGame()

    # Black Pieces
    chess_game.blackPieces.append(Rook("Black", Position(1,8), name="Rook1"))
    chess_game.blackPieces.append(Rook("Black", Position(8,8), name="Rook2"))

    chess_game.blackPieces.append(Knight("Black", Position(2,8), name="Knight1"))
    chess_game.blackPieces.append(Knight("Black", Position(7,8), name="Knight2"))

    chess_game.blackPieces.append(Bishop("Black", Position(3,8), name="Bishop1"))
    chess_game.blackPieces.append(Bishop("Black", Position(6,8), name="Bishop2"))

    chess_game.blackPieces.append(Queen("Black", Position(4,8), name="Queen"))
    chess_game.blackPieces.append(King("Black", Position(5,8), name="King"))

    chess_game.blackPieces.append(Pawn("Black", Position(1,7), name="Pawn1"))
    chess_game.blackPieces.append(Pawn("Black", Position(2,7), name="Pawn2"))
    chess_game.blackPieces.append(Pawn("Black", Position(3,7), name="Pawn3"))
    chess_game.blackPieces.append(Pawn("Black", Position(4,7), name="Pawn4"))

    chess_game.blackPieces.append(Pawn("Black", Position(5,7), name="Pawn5"))
    chess_game.blackPieces.append(Pawn("Black", Position(6,7), name="Pawn6"))
    chess_game.blackPieces.append(Pawn("Black", Position(7,7), name="Pawn7"))
    chess_game.blackPieces.append(Pawn("Black", Position(8,7), name="Pawn8"))
  
    # White Pieces
    chess_game.whitePieces.append(Rook("White", Position(1,1), name="Rook1"))
    chess_game.whitePieces.append(Rook("White", Position(8,1), name="Rook2"))

    chess_game.whitePieces.append(Knight("White", Position(2,1), name="Knight1"))
    chess_game.whitePieces.append(Knight("White", Position(7,1), name="Knight2"))

    chess_game.whitePieces.append(Bishop("White", Position(3,1), name="Bishop1"))
    chess_game.whitePieces.append(Bishop("White", Position(6,1), name="Bishop2"))

    chess_game.whitePieces.append(Queen("White", Position(4,1), name="Queen"))
    chess_game.whitePieces.append(King("White", Position(5,1), name="King"))

    chess_game.whitePieces.append(Pawn("White", Position(1,2), name="Pawn1"))
    chess_game.whitePieces.append(Pawn("White", Position(2,2), name="Pawn2"))
    chess_game.whitePieces.append(Pawn("White", Position(3,2), name="Pawn3"))
    chess_game.whitePieces.append(Pawn("White", Position(4,2), name="Pawn4"))
    chess_game.whitePieces.append(Pawn("White", Position(5,2), name="Pawn5"))
    chess_game.whitePieces.append(Pawn("White", Position(6,2), name="Pawn6"))
    chess_game.whitePieces.append(Pawn("White", Position(7,2), name="Pawn7"))
    chess_game.whitePieces.append(Pawn("White", Position(8,2), name="Pawn8"))

    
    
    chess_game.getAllPieces()
    
    # Moving Pieces
    chess_game.movePiece(chess_game.whitePieces[1], Position(3,3))  # wKnight1 b1 to c3
    chess_game.movePiece(chess_game.blackPieces[8], Position(4,5))  # bPawn5 d7 to d5
    chess_game.movePiece(chess_game.whitePieces[3], Position(4,3))  # wPawn4 d2 to d3
    chess_game.movePiece(chess_game.blackPieces[5], Position(6,5))  # bBishop2 f8 to f5
    chess_game.movePiece(chess_game.whitePieces[0], Position(1,4))  # wRook1 a1 to a4 (invalid: should print cannot move)
    chess_game.movePiece(chess_game.whitePieces[0], Position(1,3))  # wRook1 a1 to a3 (valid)

    # chess_game.whitePieces[1].move(Position(3,3))  # wKnight1 b1 to c3
    # chess_game.blackPieces[8].move(Position(4,5))  # bPawn5 d7 to d5
    # chess_game.whitePieces[3].move(Position(4,3))  # wPawn4 d2 to d3
    # chess_game.blackPieces[5].move(Position(6,5))  # bBishop2 f8 to f5
    # chess_game.whitePieces[0].move(Position(1,4))  # wRook1 a1 to a4 (invalid: should print cannot move)
    # chess_game.whitePieces[0].move(Position(1,3))  # wRook1 a1 to a3 (valid)

    print("\n***After Some Pieces Move***\n")

    print(chess_game.whitePieces[1])  # wKnight1
    print(chess_game.blackPieces[8])  # bPawn5
    print(chess_game.whitePieces[3])  # wPawn4
    print(chess_game.blackPieces[5])  # bBishop2
    print(chess_game.whitePieces[0])  # wRook1


main()

# abs()


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
    Put each class in its own file 
    Add comments to explain your code 
    Test each piece type for correct movement 
    Focus on core functionality over advanced game logic
"""