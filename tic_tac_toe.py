import joblib
import numpy
import warnings

warnings.filterwarnings('ignore')

theBoard = {
    '0': {'0': '0', '1': '0', '2': '0'},
    '1': {'0': '0', '1': '0', '2': '0'},
    '2': {'0': '0', '1': '0', '2': '0'}
}

#classifier to be used

print("Which model would you like to use")
print("1. MLPClassifier")
print("2. KNNClassifier")
print("3. svmClassifier")


modelChoice = input("Please choose 1, 2, or 3...")



if modelChoice == '1':
    Classifier = joblib.load('mlpClassifier.sav')
    print("You have chosen the MLP Classifier")
elif modelChoice == '2':
    Classifier = joblib.load('knnClassifier.sav')
    print("You have chosen the KNN Classifier")
else:
    Classifier = joblib.load('svmClassifier.sav')
    print("You have chosen the SVM Classifier")


def movePossible(board):
    empty_spaces = 0
    for r in board:
        for c in board:
            if board[r][c] == '0':
                empty_spaces = empty_spaces + 1
    if empty_spaces >= 2:
        return True
    else:
        return False


def printBoard(board):
    print('')
    print(board['0']['0'] + '|' + board['0']['1'] + '|' + board['0']['2'])
    print('-+-+-')
    print(board['1']['0'] + '|' + board['1']['1'] + '|' + board['1']['2'])
    print('-+-+-')
    print(board['2']['0'] + '|' + board['2']['1'] + '|' + board['2']['2'])
    print('')


def checkWin(board, gamer):
    # check for row wins
    for r in board:
        count = 0
        for c in board:
            if board[r][c] == gamer:
                count = count + 1
            if count == 3:
                return True
    # check for col wins
    for c in board:
        count = 0
        for r in board:
            if board[r][c] == gamer:
                count = count + 1
            if count == 3:
                return True
    # check for diag wins
    if board['1']['1'] == gamer:
        if (board['0']['0'] == gamer) and (board['2']['2'] == gamer):
            return True
        if (board['2']['0'] == gamer) and (board['0']['2'] == gamer):
            return True
    return False


def resetBoard(board):
    for r in board:
        for c in board:
            board[r][c] = '0'


def computerMove(board):
    arr = []
    for r in board:
        for c in board:
            arr.append(int(board[r][c]))
    prediction_input = numpy.array([arr])
    pred = Classifier.predict(prediction_input)[0]
    if(theBoard[str(int(pred / 3))][str(int(pred % 3))] == '0'):
        theBoard[str(int(pred / 3))][str(int(pred % 3))] = '-1'
    else:
        print("The Computer could not predict a Usable Space")

def game():
    playAgain = "y"
    while playAgain == "y":
        printBoard(theBoard)
        winner = ""
        while winner == "":
            if movePossible(theBoard):
                # player handle
                print("Player's move")
                pRow = input("Select row (enter a number 0-2): ")
                pCol = input("Select column (enter a number 0-2): ")
                if (0 <= int(pRow) <= 2) and (0 <= int(pCol) <= 2):
                    if theBoard[pRow][pCol] == '0':
                        theBoard[pRow][pCol] = '+1'
                        printBoard(theBoard)
                        if checkWin(theBoard, '+1'):
                            winner = "Player"
                        else:
                            # computer handle
                            print("Computer's move")
                            computerMove(theBoard)
                            printBoard(theBoard)
                            if checkWin(theBoard, '-1'):
                                winner = "Computer"
                    else:
                        print("This space is already taken!")
                else:
                    print("Invalid input! Try again")
            else:
                print("It's a tie!")
                winner = "No one"
        print(winner + ' is the winner!')
        print('')
        playAgain = input("Would you like to play again (y/n): ")
        resetBoard(theBoard)


if __name__ == "__main__":
    game()
