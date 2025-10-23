# LM Chess Classes (Pieces mainly)
from abc import ABC, abstractmethod

class ChessGame:
    def __init__(self, whitePieces, blackPieces):
        self.whitePieces = whitePieces
        self.blackPieces = blackPieces
    
    def movePiece(self):
        pass

    def removePlace(self):
        pass

    def getPiecesLeft(self):
        pass

    def getPiecesAt(self):
        pass


class ChessPiece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
    
    def getPos(self):
        return

    @abstractmethod
    def move(self, newPos): #bool
        self.position = newPos

    @abstractmethod
    def getSymbol(self):
        pass

    # def __str__():
    #     return f""


class Pawn(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(newPos):
        pass

    def getSymbol():
        return "p"
    
class Rook(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(newPos):
        pass

    def getSymbol():
        return "r"
    
class Knight(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(newPos):
        pass

    def getSymbol(self):
        return "k"
    
class Bishop(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        pass

    def getSymbol():
        return "b"
        
class Queen(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        pass

    def getSymbol(self):
        return "Q"

class King(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def canMoveTo(self, newPos):
        pass

    def getSymbol(self):
        return "K"