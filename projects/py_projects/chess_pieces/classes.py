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


    



class ChessPiece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
    
    def getPos(self):
        return self.position

    @abstractmethod
    def move(self, newPos):
        pass

    @abstractmethod
    def getSymbol(self):
        pass

    def __str__(self):
        return f"{self.color} {self.getSymbol()} at {self.position}"


class Pawn(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        # pawn movement logic
        if self.color == "White":
            if newPos.column == self.position.column and newPos.row == self.position.row + 1:
                return True
        else:  # Black pawn
            if newPos.column == self.position.column and newPos.row == self.position.row - 1:
                return True
        return False
    
    def move(self, newPos):
        if self.canMoveTo(newPos):
            self.position = newPos
            return True
        return False
            

    def getSymbol(self):
        return "p"
    
class Rook(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        if newPos.column == self.position.column or newPos.row == self.position.row:
            return True
        return False
    
    def move(self, newPos):
        if self.canMoveTo(newPos):
            self.position = newPos
            return True
        return False

    def getSymbol(self):
        return "r"
    
class Knight(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        if (abs(newPos.column - self.position.column) == 2 and abs(newPos.row - self.position.row) == 1) or (abs(newPos.column - self.position.column) == 1 and abs(newPos.row - self.position.row) == 2):
            return True
        return False
    
    def move(self, newPos):
        if self.canMoveTo(newPos):
            self.position = newPos
            return True
        return False

    def getSymbol(self):
        return "k"
    
class Bishop(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        if abs(newPos.column - self.position.column) == abs(newPos.row - self.position.row):
            return True
        return False
    
    def move(self, newPos):
        if self.canMoveTo(newPos):
            self.position = newPos
            return True
        return False

    def getSymbol():
        return "b"
        
class Queen(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        if (newPos.column == self.position.column or newPos.row == self.position.row) or (abs(newPos.column - self.position.column) == abs(newPos.row - self.position.row)):
            return True
        return False

    def move(self, newPos):
        if self.canMoveTo(newPos):
            self.position = newPos
            return True
        return False

    def getSymbol(self):
        return "Q"

class King(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        if abs(newPos.column - self.position.column) <= 1 and abs(newPos.row - self.position.row) <= 1:
            return True
        return False
    
    def move(self, newPos):
        if self.canMoveTo(newPos):
            self.position = newPos
            return True
        return False

    def getSymbol(self):
        return "K"
    



class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
    
    def placePiece(self, piece, position):
        col = position.column - 1
        row = position.row - 1
        self.grid[row][col] = piece
    
    def removePiece(self, position):
        col = position.column - 1
        row = position.row - 1
        self.grid[row][col] = None
    
    def getPieceAt(self, position):
        col = position.column - 1
        row = position.row - 1
        return self.grid[row][col]


class ChessGame:
    def __init__(self, whitePieces, blackPieces):
        self.whitePieces = whitePieces
        self.blackPieces = blackPieces

    def removePieces(self):
        otherPiece = self.getPiecesAt(self.position)
        if self.position == otherPiece.position:
            if self.color != otherPiece.color:
                otherPiece = None
                self.removePiece(self.position)
            
        
    def movePiece(self, newPos):
        if self.canMoveTo():
            self.position = newPos
            self.removePieces()
            return True
        return False
    
    def getPiecesLeft(self):
        for piece in self.whitePieces:
            if piece is not None:
                return len(self.whitePieces)
        for piece in self.blackPieces:
            if piece is not None:
                return len(self.blackPieces)
            

    def getPiecesAt(self):
        for piece in self.whitePieces:
            if piece.position == self.position:
                return piece
        for piece in self.blackPieces:
            if piece.position == self.position:
                return piece