from piece import *
import serialComm/SerialComm

class Board():

    def __init__(self):
        #Board initialization code
        self.board = [[0 for x in xrange(8)] for x in xrange(8)]

        self.board[0][0] = Rook(0, 0, "white", "Rook")
        self.board[7][0] = Rook(7, 0, "white", "Rook")
        self.board[1][0] = Knight(1, 0, "white", "Knight")
        self.board[6][0] = Knight(6, 0, "white", "Knight")
        self.board[2][0] = Bishop(2, 0, "white", "Bishop")
        self.board[5][0] = Bishop(5, 0, "white", "Bishop")
        self.board[3][0] = Queen(3, 0, "white", "Queen")
        self.board[4][0] = King(4, 0, "white", "King")
        for i in xrange(0,8):
            self.board[i][1] = Pawn(i, 1, "white", "Pawn")

        self.board[0][7] = Rook(0, 7, "black", "Rook")
        self.board[7][7] = Rook(7, 7, "black", "Rook")
        self.board[1][7] = Knight(1, 7, "black", "Knight")
        self.board[6][7] = Knight(6, 7, "black", "Knight")
        self.board[2][7] = Bishop(2, 7, "black", "Bishop")
        self.board[5][7] = Bishop(5, 7, "black", "Bishop")
        self.board[3][7] = Queen(3, 7, "black", "Queen")
        self.board[4][7] = King(4, 7, "black", "King")
        for i in xrange(0,8):
            self.board[i][6] = Pawn(i, 6, "black", "Pawn")

    def checkValidMove(self, x, y, newX, newY, colorTurn):
        piece = self.board[x][y]
        if(piece == 0):
            return False
        elif(x == newX and y == newY):
            return False
        elif(piece.get_color() != colorTurn):
            return False
        elif(not piece.move(newX, newY)):
            return False
 
        #Vertical
        if(x == newX):
            for i in range(piece.get_y(), newY):
                if i != piece.get_y() and self.board[x][i]:
                    return False       
            return self.takeLastPiece(piece, newX, newY, False) 

        #Horizontal
        elif(y == newY):
            for i in range(piece.get_x(), newX):
                if i != piece.get_x() and self.board[i][y]:
                    return False
            return self.takeLastPiece(piece, newX, newY, False)

        #Knight
        elif(piece.get_name() == "Knight"):
            if(self.board[newX][newY] == 0 or self.board[newX][newY].get_color() != piece.get_color()):
                if(abs(piece.get_x() - newX) == 2):
                    dir = 1 if(piece.get_x() < newX) else - 1
                    coordinates = self.move_for_knight(x + dir, y, newX, newY)
                else:
                    dir = 1 if(piece.get_y() < newY) else - 1
                    coordinates = self.move_for_knight(x, y + dir, newX, newY)
                if(coordinates):
                    if(self.board[newX][newY] != 0):
                        self.move_piece_off_board(newX, newY)
                else:
                    return False 
            else:
                return False

            if(abs(piece.get_x() - newX) == 2):
                dir = 1 if(piece.get_x() < newX) else -1
                self.move_piece_serial(x , y, x + dir, y)
                self.move_piece_serial(x + dir, y, newX, newY)
                piece.update_coordinate(newX, newY)
            else:
                dir = 1 if(piece.get_y() < newY) else -1
                self.move_piece_serial(x, y, x, y + dir)
                self.move_piece_serial(x,  y + dir, newX, newY)
                piece.update_coordinate(newX, newY)
            
            self.board[newX][newY] = piece
            if(len(coordinates) == 4):
                self.board[coordinates[0]][coordinates[1]] = self.board[coordinates[2]][coordinates[3]]
                self.move_piece_serial(coordinates[2], coordinates[3], coordinates[0], coordinates[1])
            return True

        #Diagonal
        else:
            xDir = 1 if(piece.get_x() < newX) else -1
            yDir = 1 if(piece.get_y() < newY) else -1
            lateralDist = abs(newX - piece.get_x())
            for i in range(0, lateralDist):
                if(i != 0 and self.board[piece.get_x() + xDir * i][piece.get_y() + yDir * i]):
                    return False
            return self.takeLastPiece(piece, newX, newY, piece.get_name() == "Pawn")

    def takeLastPiece(self, piece, newX, newY, isPawnDiag):
        if(isPawnDiag):
            if(self.board[newX][newY] == 0 or self.board[newX][newY].get_color() == piece.get_color()):
                piece.decrementMoves()
                return False 
        elif(self.board[newX][newY] != 0 and (self.board[newX][newY].get_color() == piece.get_color() or piece.get_name() == "Pawn")):
            return False
        
        self.board[piece.get_x()][piece.get_y()] = 0
        if(self.board[newX][newY] != 0):
            self.move_piece_off_board(newX, newY)
            #Handle move off board    
        self.move_piece_serial(piece.get_x(), piece.get_y(), newX, newY)
        self.board[newX][newY] = piece
        piece.update_coordinate(newX, newY)
        return True      

    #Pass coordinates for serial movement
    def move_piece_serial(self, x, y, newX, newY):
        self.board[x][y] = 0
        pass

    def move_piece_off_board(self, newX, newY):
        print "move off board"
        left =0
        right = 0
        stack = []
        for i in range(0, 8):
            if i < newX and self.board[i][newY]:
                left += 1
            if i > newX and self.board[i][newY]:
                right += 1
        if left < right:
            for i in range(0, newX):
                if self.board[i][newY]:
                    stack.append(self.move_for_knight(i, newY, i, newY))
            self.move_piece_serial(newX, newY, -1, newY)        
        else:
            for i in range(newX+1, 8):
                if self.board[i][newY]:
                    stack.append(self.move_for_knight(i, newY, i, newY))
            self.move_piece_serial(newX, newY, 9, newY)        

        while stack:
            temp = stack.pop()
            self.board[temp[0]][temp[1]] = self.board[temp[2]][temp[3]]
            self.move_piece_serial(temp[2], temp[3], temp[0], temp[1])          
        
        self.board[newX][newY] = 0


        pass
 
    def move_for_knight(self, x, y, finalX, finalY):
        if(self.board[x][y] == 0):
            return (1, 2)
        piece = self.board[x][y]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.board[x + i][y + j] == 0 and (x + i != finalX or y + j != finalY)):   
                    self.move_piece_serial(x, y, x + i, y + j)
                    self.board[x + i][y + j] = piece  
                    return (x, y, x + i, y + j)
        print("Currently can't make room for the knight")
        return() 

    def printBoard(self):
        for i in range(0, 8):
            print ""
            for j in range(0, 8):
                if(self.board[j][7 - i] == 0):
                    print("0"),
                else:
                    print(self.board[j][7 - i].get_name()[0]),









