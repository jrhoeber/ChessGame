import chess

class Board():

    def __init__(self):
        #Board initialization code

    def checkValidMove(piece, newX, newY, colorTurn):
        if(piece.get_color() != colorTurn):
            return false

        if(x == newX):
            for i in range(piece.get_x(), newX):
                if i != piece.get_x() and gameBoard[y][i]:
                    return False       
            takeLastPiece(piece, newX, newY) 

        elif(y == newY):
            for i in range(piece.get_y(), newY):
                if i != piece.get_y() and gameBoard[i][x]:
                    return False
            takeLastPiece(piece, newX, newY)

        elif(piece.get_name() == "Knight"):
            takeLastPiece(piece, newX, newY)

        else:

    def takeLastPiece(piece, newX, newY):
        if(gameBoard[newY][newX] and gameBoard[newY][newX].get_color() == piece.get_color()):
            return False
        else:
            return True      



