import readAudio as audio
from board import Board 

def LetterToInt(letter):
    letters = "abcdefghi"
    return letters.index(letter.lower())


if __name__ == "__main__":
    board = Board()
    colors = ("white", "black")
    count = 0
    while True:
        print colors[count % 2]
        move = audio.getMove()
        if move:
            valid = board.checkValidMove(LetterToInt(move[0]), move[1] - 1, LetterToInt(move[2]), move[3] - 1, colors[count % 2])
            board.printBoard()
            if valid:
                 count += 1
