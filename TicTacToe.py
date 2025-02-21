import random

def CheckIfBoardIsFullyOccupied(board: dict[str]) -> bool:
    """THE BELOW IS THE DEFAULT CODE I HAVE WRITTEN AND THEN LATER FOUND BETTER APPROACH"""
    # occupiedValues: int = 0

    # for value in board.values():
    #     if (value != ' '):
    #         occupiedValues += 1

    # return occupiedValues == len(board.values())

    # return ' ' not in board.values() #ALSO A BETTER APPROACH

    return not list(board.values()).__contains__(' ')


def printBoard(board) -> None:
    print(f'{board['top-L']}|{board['top-M']}|{board['top-R']}')
    print('-+-+-')
    print(f'{board['mid-L']}|{board['mid-M']}|{board['mid-R']}')
    print('-+-+-')
    print(f'{board['low-L']}|{board['low-M']}|{board['low-R']}')


def getRemainingMoves(board: dict[str]) -> str:
    """OLD IMPLEMENTATION"""
    # remainingMoves: str = ''

    # for move in board.keys():
    #     if (board[move] != ' '):
    #         continue
    #     if (remainingMoves == ''):
    #         remainingMoves += move
    #     else:
    #         remainingMoves += f', {move}'

    # return remainingMoves

    """NEW IMPROVED IMPLEMENTATION"""
    # print(str([move for move in board.keys() if(board[move] == ' ')]))
    # [new_item for item in iterable if condition]
    # print(", ".join([move for move in board.keys() if board[move] == ' ']))
    # print(", ".join([move if board[move] == ' ' else "Not Empty" for move in board.keys()]))

    return ", ".join([move for move in board.keys() if board[move] == ' '])


def findWinner(users: list[str], board: dict[str]) -> str | None:

    for user in users:
        # HORIZONTAL
        if (board['top-L'] == user and board['top-M'] == user and board['top-R'] == user):
            return user
        elif (board['mid-L'] == user and board['mid-M'] == user and board['mid-R'] == user):
            return user
        elif (board['low-L'] == user and board['low-M'] == user and board['low-R'] == user):
            return user

        # VERTICAL
        elif (board['top-L'] == user and board['mid-L'] == user and board['low-L'] == user):
            return user
        elif (board['top-M'] == user and board['mid-M'] == user and board['low-M'] == user):
            return user
        elif (board['top-R'] == user and board['mid-R'] == user and board['low-R'] == user):
            return user

        # DIAGONAL
        elif (board['top-L'] == user and board['mid-M'] == user and board['low-R'] == user):
            return user
        elif (board['top-R'] == user and board['mid-M'] == user and board['low-L'] == user):
            return user

    return None


def StartTicTacToeGame():

    USERS = ['O', 'X']

    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    # value_if_true if condition else value_if_false

    # UserTurn = 'O' if random.randint(0, 1) == 0 else 'X'

    UserTurn = USERS[random.randint(0, 1)]

    isOccupied = False

    while (True):

        isOccupied = CheckIfBoardIsFullyOccupied(theBoard)
        if (isOccupied):
            print('No more place left on the board so it is a tie.')
            break
        printBoard(theBoard)
        remainingMoves = getRemainingMoves(theBoard)

        print(
            f'Dear USER:{UserTurn} Please enter your desired move given the remaning moves are: {remainingMoves}')

        newMove = input()

        if (newMove not in remainingMoves):
            print('Wrong move, Please try again')
            continue

        theBoard[newMove] = UserTurn

        winner = findWinner(USERS, theBoard)

        print(winner)
        if (winner in USERS):
            print(f'Yay Congratulations to the winner : {UserTurn}')
            printBoard(theBoard)
            break

        UserTurn = 'O' if UserTurn == 'X' else 'X'


StartTicTacToeGame()
