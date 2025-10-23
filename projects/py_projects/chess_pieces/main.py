# LM  Chess Pieces Project
from classes import *

board = [ ["r","n","b","q","k","b","n","r"],
        ["p","p","p","p","p","p","p","p"],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "],
        ["P","P","P","P","P","P","P","P"],
        ["R","N","B","Q","K","B","N","R"] ]

def main(): # Creates Objects 

    bRook1 = Rook("Black", "a8")
    bRook2 = Rook("Black", "h8")

    bKnight1 = Knight("Black", "b8")
    bKnight2 = Knight("Black", "g8")

    bBishop1 = Bishop("Black", "c8")
    bBishop2 = Bishop("Black", "f8")

    bQueen = Queen("Black", "d8")
    bKing = King("Black", "e8")

    bPawn1 = Pawn("Black", "a7")
    bPawn2 = Pawn("Black", "b7")
    bPawn3 = Pawn("Black", "c7")
    bPawn4 = Pawn("Black", "d7")

    bPawn5 = Pawn("Black", "e7")
    bPawn6 = Pawn("Black", "f7")
    bPawn7 = Pawn("Black", "g7")
    bPawn8 = Pawn("Black", "h7")


    wRook1 = Rook("White", "a1")
    wRook2 = Rook("White", "h1")

    wKnight1 = Knight("White", "b1")
    wKnight2 = Knight("White", "g1")

    wBishop1 = Bishop("White", "c1")
    wBishop2 = Bishop("White", "f1")

    wQueen = Queen("White", "d1")
    wKing = King("White", "e1")

    wPawn1 = Pawn("White", "a2")
    wPawn2 = Pawn("White", "b2")
    wPawn3 = Pawn("White", "c2")
    wPawn4 = Pawn("White", "d2")

    wPawn5 = Pawn("White", "e2")
    wPawn6 = Pawn("White", "f2")
    wPawn7 = Pawn("White", "g2")
    wPawn8 = Pawn("White", "h2")


    wPawn1.move()
    bPawn1.move()
    wPawn8.move()
    bPawn8.move()
    wRook2.move()

    

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