# LM Chess Classes (Pieces mainly)
from abc import ABC, abstractmethod

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row
    
    def getColumn(self):
        if self.column == 1:
            return "a"
        elif self.column == 2:
            return "b"
        elif self.column == 3:
            return "c"
        elif self.column == 4:
            return "d"
        elif self.column == 5:
            return "e"
        elif self.column == 6:
            return "f"
        elif self.column == 7:
            return "g"
        elif self.column == 8:
            return "h"
        
    def getRow(self):
        return self.row
    
    def __str__(self):
        return f"{self.getColumn()}{self.getRow()}"
    
    def __eq__(self, other):
        return self.column == other.column and self.row == other.row




class ChessPiece(ABC):
    def __init__(self, color, position, name=""):
        self.color = color
        self.position = position
        self.name = name
    
    def getPos(self):
        return self.position

    @abstractmethod
    def canMoveTo(self, newPos):
        pass

    # @abstractmethod
    # def move(self, newPos):
    #     pass

    @abstractmethod
    def getSymbol(self):
        pass

    def __str__(self):
        return f"{self.color} {self.name}, Symbol {self.getSymbol()} is at {self.position}"


class Pawn(ChessPiece):
    def __init__(self, color, position, name="Pawn"):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        # pawn movement logic
        # How do you check for if there is already a piece of the same color? Answer: You would need access to the board state to check for other pieces. How would you do that?: You would need to pass the board state or have a reference to it within the piece class.
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
        return "p"
    
class Rook(ChessPiece):
    def __init__(self, color, position, name="Rook"):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        if newPos.column == self.position.column or newPos.row == self.position.row:
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        return "r"
    
class Knight(ChessPiece):
    def __init__(self, color, position, name="Knight"):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        if (abs(newPos.column - self.position.column) == 2 and abs(newPos.row - self.position.row) == 1) or (abs(newPos.column - self.position.column) == 1 and abs(newPos.row - self.position.row) == 2):
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        return "k"
    
class Bishop(ChessPiece):
    def __init__(self, color, position, name="Bishop"):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        if abs(newPos.column - self.position.column) == abs(newPos.row - self.position.row):
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        return "b"
        
class Queen(ChessPiece):
    def __init__(self, color, position, name="Queen"):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        if (newPos.column == self.position.column or newPos.row == self.position.row) or (abs(newPos.column - self.position.column) == abs(newPos.row - self.position.row)):
            return True
        return False

    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        return "Q"

class King(ChessPiece):
    def __init__(self, color, position, name="King"):
        super().__init__(color, position, name)

    def canMoveTo(self, newPos):
        if abs(newPos.column - self.position.column) <= 1 and abs(newPos.row - self.position.row) <= 1:
            return True
        return False
    
    # def move(self, newPos):
    #     if self.canMoveTo(newPos):
    #         self.position = newPos
    #         return True
    #     return False

    def getSymbol(self):
        return "K"
    



# class Board:
#     def __init__(self):
#         self.grid = [[None for _ in range(8)] for _ in range(8)]
    
#     def placePiece(self, piece, position):
#         col = position.column - 1
#         row = position.row - 1
#         self.grid[row][col] = piece
    
#     def removePiece(self, position):
#         col = position.column - 1
#         row = position.row - 1
#         self.grid[row][col] = None
    
#     def getPieceAt(self, position):
#         col = position.column - 1
#         row = position.row - 1
#         return self.grid[row][col]


class ChessGame:
    def __init__(self):
        self.whitePieces = []
        self.blackPieces = []

    def movePiece(self, piece, newPos): # return Bool
        if piece.canMoveTo(newPos): #  it should check if there is an opponent piece at the new position
            if self.removePiece(piece, self.getPiecesAt(piece.position)) == True:
                piece.position = newPos
                return True
        return False

    def removePiece(self,piece, otherPiece=None):
        if otherPiece != None:
            if otherPiece.color == piece.color:
                return False  # Cannot capture own piece
            else:
                if piece in self.whitePieces:
                    self.whitePieces.remove(piece)
                elif piece in self.blackPieces:
                    self.blackPieces.remove(piece)
        return True
    
    def getPiecesLeft(self, color): # return List
        if color == "White":
            return len(self.whitePieces)
        elif color == "Black":
            return len(self.blackPieces)

    def getPiecesAt(self, pos): # return Piece
        for piece in self.whitePieces + self.blackPieces:
            if piece.position == pos: # Both have to be objects of Position class
                return piece
        return None
            
    def getAllPieces(self):
        for piece in self.blackPieces:
            print(piece)

        print()
        
        for piece in self.whitePieces:
            print(piece)