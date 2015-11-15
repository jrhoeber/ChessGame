#import readAudio
from board import Board 

if __name__ == "__main__":
    board = Board()
    color = "white"
    print board.checkValidMove(0, 1, 0, 2, color)
    print board.checkValidMove(1, 0, 0, 2, color)

