#import readAudio
from board import Board 

if __name__ == "__main__":
    board = Board()
    color = "white"
    print board.checkValidMove(0, 1, 0, 6, color)
    print board.checkValidMove(0, 6, 0, 7, color)

