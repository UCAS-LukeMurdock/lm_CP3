# LM Chess Classes (Pieces mainly)
from abc import ABC, abstractmethod

class Position: # Represents a position on the chess board
    def __init__(self, column, row):
        self.column = column
        self.row = row
    
    def getColumn(self): # Method to convert column number to letter
        if self.column == 1:
            return "A"
        elif self.column == 2:
            return "B"
        elif self.column == 3:
            return "C"
        elif self.column == 4:
            return "D"
        elif self.column == 5:
            return "E"
        elif self.column == 6:
            return "F"
        elif self.column == 7:
            return "G"
        elif self.column == 8:
            return "H"
        
    def getRow(self):
        return self.row
    
    def __str__(self): # String representation of position
        return f"{self.getColumn()}{self.getRow()}"
    
    def __eq__(self, other): # Equality check for positions
        return self.column == other.column and self.row == other.row




class ChessPiece(ABC): # Abstract Base Class for Chess Pieces
    def __init__(self, color, position, name=""):
        self.color = color
        self.position = position
        self.name = name
    
    def getColor(self): # return String color
        return self.color

    def getPos(self): # return String of position
        return f"{self.getColor()} {self.name}, Symbol {self.getSymbol()}  is at {self.position}"

    def setPosition(self, newPos): # Set the piece to a new position
        self.position = newPos

    @abstractmethod
    def canMoveTo(self, newPos): # Method to check if piece can move to newPos
        pass

    # @abstractmethod
    # def move(self, newPos):
    #     pass

    @abstractmethod
    def getSymbol(self): # return String symbol
        pass

    def __str__(self): # String representation of piece
        return f"{self.getColor()} {self.name}"


class Pawn(ChessPiece): # Pawn Class
    def __init__(self, color, position, name):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        # Can only move forward one square
        if self.color == "White":
            if newPos.column == self.position.column and newPos.row == self.position.row + 1:
                return True
        else:  # Black pawn
            if newPos.column == self.position.column and newPos.row == self.position.row - 1:
                return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False
            
    def getSymbol(self):
        if self.color == "White":
            return "♟"
        elif self.color == "Black":
            return "♙"
    
class Rook(ChessPiece): # Rook Class
    def __init__(self, color, position, name):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        # Rook can move any number of squares along a row or column
        if newPos.column == self.position.column or newPos.row == self.position.row:
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        if self.color == "White":
            return "♜"
        elif self.color == "Black":
            return "♖"
    
class Knight(ChessPiece): # Knight Class
    def __init__(self, color, position, name):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        # Knight moves in an "L" shape: two squares in one direction and then one square perpendicular
        column_diff = abs(newPos.column - self.position.column)
        row_diff = abs(newPos.row - self.position.row)
        if (column_diff == 2 and row_diff == 1) or (column_diff == 1 and row_diff == 2):
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        if self.color == "White":
            return "♞"
        elif self.color == "Black":
            return "♘"

class Bishop(ChessPiece): # Bishop Class
    def __init__(self, color, position, name):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        # The change in columns and rows must be equal.
        if abs(newPos.column - self.position.column) == abs(newPos.row - self.position.row):
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        if self.color == "White":
            return "♝"
        elif self.color == "Black":
            return "♗"
        
class Queen(ChessPiece): # Queen Class
    def __init__(self, color, position, name):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        # Like Rook (horizontal and vertical) [same row or same column]
        if newPos.column == self.position.column or newPos.row == self.position.row:
            return True
        
        # Like Bishop (diagonal) [change in columns equals change in rows]
        elif abs(newPos.column - self.position.column) == abs(newPos.row - self.position.row):
            return True
        
        return False

    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        if self.color == "White":
            return "♛"
        elif self.color == "Black":
            return "♕"

class King(ChessPiece): # King Class
    def __init__(self, color, position, name):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        # King can move one square in any direction
        column_diff = abs(newPos.column - self.position.column)
        row_diff = abs(newPos.row - self.position.row)
        if column_diff <= 1 and row_diff <= 1:
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        if self.color == "White":
            return "♚"
        elif self.color == "Black":
            return "♔"


class ChessGame: # Chess Game Class
    def __init__(self):
        self.whitePieces = []
        self.blackPieces = []

    # Moves a piece to a new position if the move is valid and handles captures
    def movePiece(self, piece, newPos): # return Bool
        if piece.canMoveTo(newPos):
            if self.removePiece(piece, self.getPieceAt(newPos)) == True:
                oldPos = piece.position
                piece.setPosition(newPos)
                print(f"Moved {piece} from {oldPos} to {newPos}")
                print(self.getBoard())
                return True
        print(f"Cannot move {piece} from {piece.position} to {newPos}\n\t(Either doesn't follow movement rules or position blocked by same-colored piece)")
        return False
    
    # Removes a piece from the game if it is captured
    def removePiece(self,piece, otherPiece=None):
        if otherPiece != None:
            if otherPiece.color == piece.color:
                return False  # Cannot capture own piece
            else:
                if otherPiece in self.whitePieces:
                    self.whitePieces.remove(otherPiece)
                    print(f"{otherPiece} captured by {piece}!\n\tBlack Pieces Left: {self.getPiecesAmountLeft('Black')} | White Pieces Left: {self.getPiecesAmountLeft('White')}")
                elif otherPiece in self.blackPieces:
                    self.blackPieces.remove(otherPiece)
                    print(f"{otherPiece} captured by {piece}!\n\tBlack Pieces Left: {self.getPiecesAmountLeft('Black')} | White Pieces Left: {self.getPiecesAmountLeft('White')}")
        return True
    
    # Method that returns string of pieces left
    def getPiecesLeft(self, color = ""): # return List?
        pieces_left = ""
        if color == "White":
            for piece in self.whitePieces:
                pieces_left += str(piece) + ", "
        elif color == "Black":
            for piece in self.blackPieces:
                pieces_left += str(piece) + ", "
        else:
            for piece in self.whitePieces + self.blackPieces:
                pieces_left += str(piece) + ", "

        return f"{color} Pieces Left: {pieces_left[:-2]}"
    
    # Method that returns amount of pieces left
    def getPiecesAmountLeft(self, color): # return Int
        if color == "White":
            return len(self.whitePieces)
        elif color == "Black":
            return len(self.blackPieces)

    # Method that returns a piece at a given position
    def getPieceAt(self, pos): # return Piece
        for piece in self.whitePieces + self.blackPieces:
            if piece.position == pos: # Both have to be objects of Position class
                return piece
        return None

    # Method that prints all pieces and their positions
    def getAllPieces(self):
        pieces = "\nBlack Pieces:\n"
        for piece in self.blackPieces:
            pieces += piece.getPos() + "\n"

        pieces += "\nWhite Pieces:\n"
        
        for piece in self.whitePieces:
            pieces += piece.getPos() + "\n"
        return pieces
    
    # Method that returns a string representation of the board
    def getBoard(self): # return String
        board = "\n"
        for row in range(8, 0, -1):
            for col in range(1, 9):
                piece = self.getPieceAt(Position(col, row))
                if piece != None:
                    board += piece.getSymbol() + " "
                else:
                    board += ". "
            board += "\n"
        return board
    
    # String representation of the game status
    def __str__(self):
        return f"This Chess Game currently has {self.getPiecesAmountLeft('White')} White pieces left and {self.getPiecesAmountLeft('Black')} Black pieces left.\n"
        