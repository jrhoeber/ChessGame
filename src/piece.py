class Piece(object):
    def __init__(self, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        print "Starting x: ", x, " y: ", y
    def update_coordinate(self, x,y):
        self.x = x;
        self.y = y;
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name 

class King(Piece):
    def __init__(self,x, y, color, name):
        super(King, self).__init__(x, y, color, name)
        #Ignoring castle for now
        def move(self, x, y):
            if(abs(self.x - x) == 1 or abs(self.y - y) == 1):
                return True 
            else:
                return False 

class Queen(Piece):
    def __init__(self,x, y, color, name):
        super(Queen, self).__init__(x, y, color, name)
        def move(self, x, y):
            if(self.x == x or self.y == y or abs(self.x - x) == abs(self.y - y)):
                return True
            else:
                return False 

class Rook(Piece):
    def __init__(self,x, y, color, name):
        super(Rook, self).__init__(x, y, color, name)
        def move(self, x, y):
            if(self.x == x or self.y == y):
                return True
            else:
                return False                       

class Bishop(Piece):
    def __init__(self,x, y, color, name):
        super(Bishop, self).__init__(x, y, color, name)
    def move(self, x, y):
        for i in range(1, 8):
            if self.x+i == x and self.y+i == y:
                return True
            elif self.x+i == x and self.y-i == y:
                return True
            elif self.x-i == x and self.y+i == y:
                return True
            elif self.x-i == x and self.y-i == y:
                return True
        else:
            return False

class Knight(Piece):
    def __init__(self,x, y, color, name):
        super(Knight, self).__init__(x, y, color, name)
    def move(self, x, y):
        if (self.x+2 or self.x-2) == x and (self.y+1 or self.y-1) == y:
            return True
        elif (self.y+2 or self.y-2) == y and (self.x+1 or self.x-1) == x:
            return True
        else:
           return False

class Pawn(Piece):
    def __init__(self,x, y, color, name):
        super(Pawn, self).__init__(x, y, color, name)
        firstMove = True;
    def move(self, x, y):
        print self.color
        if self.color == "black":
            #this could be problematic
            if y == self.y-2 and firstMove:
                return true
            elif y == self.y-1:
                return True
            else:
                return False
        else:
            if y == self.y+2 and firstMove:
                return True
            elif y == self.y+1:
                return True
            else:
                return False


#check if piece is move is true, if so then copy the class in that cell
#to the new spot

#to check pawn diagonal move add a check in the board logic method?
# in board logic method, need to check and make sure the movement spot is 
# not a friendly

def LetterToInt(letter):
    letters = "abcdefghi"
    return letters.index(letter.lower())

