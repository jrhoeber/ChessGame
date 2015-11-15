from piece import *

class Board():

    def __init__(self):
        #Board initialization code
        board = [[0 for x in xrange(8)] for x in xrange(8)]

        board[0][0] = Rook(0, 0, "white")
        board[7][0] = Rook(7, 0, "white")
        board[1][0] = Knight(1, 0, "white")
        board[6][0] = Knight(6, 0, "white")
        board[2][0] = Bishop(2, 0, "white")
        board[5][0] = Bishop(5, 0, "white")
        board[3][0] = Queen(3, 0, "white")
        board[4][0] = King(4, 0, "white")
        for i in xrange(0,8):
            board[i][1] = Pawn(i, 1, "white")

        board[0][7] = Rook(0, 7, "black")
        board[7][7] = Rook(7, 7, "black")
        board[1][7] = Knight(1, 7, "black")
        board[6][7] = Knight(6, 7, "black")
        board[2][7] = Bishop(2, 7, "black")
        board[5][7] = Bishop(5, 7, "black")
        board[3][7] = Queen(3, 7, "black")
        board[4][7] = King(4, 7, "black")
        for i in xrange(0,8):
            board[i][1] = Pawn(i, 6, "black")

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



