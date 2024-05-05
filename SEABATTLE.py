#game one
import random

respond = None
game_over = False
num_ships= 0
board_size=1

while True:
    print('Hi and welcome to the game!')

    board_size = int(input('How big board do you want? (NxN size type)\n'))
    while board_size<=1:
        print('Board size must be 2x2 or bigger and must be a positive integer')
        board_size = int(input('How big board do you want? (NxN size type)\n'))

    num_ships = int(input('How many enemies do you want to have?\n'))
    amount_of_attempts = int(input('How many tries do you want to have?\n'))+1

    if board_size**2>num_ships and amount_of_attempts-1<board_size**2:
        print(f'\n\n\nYou have {amount_of_attempts} tries to sink the enemy fleet where there are {num_ships} ships!\nGood Luck!')
        break
    else:
        print(f'Provide number of enemies, that will be really to place and still have 1 free space. Also provide number of attemps, which maximum is equal to max of enemies')
        continue

def GenEnemies(board_size, existing_ships):
    while True:
        new_ship = (random.randint(1, board_size), random.randint(1, board_size))
        if new_ship not in existing_ships:
            existing_ships.append(new_ship)
            return new_ship

def print_board(board):
    print("   " + "     ".join(str(i + 1) for i in range(len(board))))
    print("  " + "-" * (4 * len(board) - 1)+"-"*5)
    for i, row in enumerate(board, start=1):
        print(f"{i:2} |{'|'.join(cell for cell in row)}"+"|")
        print("  " + "-" * (4 * len(row) - 1)+"-"*5)


def take_user_input():
    return int(input(f"Provide row number (1-{board_size}): ")), int(input(f"Provide column number (1-{board_size}): "))

def check_guess(board, enemies, guess_row, guess_col):

    global amount_of_attempts

    if (guess_col, guess_row) in enemies:
        print('BullsEye!')
        board[guess_row-1][guess_col-1] = ' X '
        enemies.remove((guess_col, guess_row))
        if not enemies:
            print_board(board)
            return 'Congratulations! You\'ve sunk all the enemy ships and won the game!'
        amount_of_attempts -= 1
    else:
        if (guess_row < 1 or guess_row > board_size) or (guess_col < 1 or guess_col > board_size):
            print("Don't shoot out of the board!")
            amount_of_attempts -= 1
        elif board[guess_row-1][guess_col-1] == " O ":
            print("You already shot there!")
            amount_of_attempts -= 1
        else:
            print("Missed!")
            board[guess_row-1][guess_col-1] = " O "
            amount_of_attempts -= 1
    return None





# Initializing board
board = [['    '] * board_size for _ in range(board_size)]

# Creating enemies
enemies = [GenEnemies(board_size, []) for _ in range(num_ships)]
while not game_over:
    for _ in range(amount_of_attempts):
        print_board(board)
        guess_row, guess_col = take_user_input()
        respond = check_guess(board, enemies, guess_row, guess_col)

        if respond:
            print(respond)
            game_over = True  # Set game_over flag to True when the player wins
            break  # Break out of the loop after a successful guess
        elif amount_of_attempts - 1 == 0:
            print("You are out of ammo. End of the game, loser. Wanna play again?")
            game_over = True
            '''
            while True:
                a = input('1 - Yes; 2 - No: ')
                if a == '1':
                    break  # Exit the loop and continue the game
                elif a == '2':
                    game_over = True
                    break  # Exit the loop and end the game
                else:
                    print('Error. You provided the wrong type of data')
                    game_over=True
                    break
            '''

if game_over:
    print('Game Over!')
    if game_over:
        print('Game Over!')
#seabattle game
#I know, that it works.
