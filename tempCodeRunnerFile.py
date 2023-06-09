board = [' '] * 9
flag = 0
count = 0


def check_sol():
    row_1 = '{}|{}|{}'.format(board[0], board[1], board[2])
    row_2 = '{}|{}|{}'.format(board[3], board[4], board[5])
    row_3 = '{}|{}|{}'.format(board[6], board[7], board[8])
    diag_1 = '{}|{}|{}'.format(board[0], board[4], board[8])
    diag_2 = '{}|{}|{}'.format(board[2], board[4], board[6])

    global flag
    if row_1 == 'x|x|x' or row_1 == 'o|o|o':
        flag = 1
    elif row_2 == 'x|x|x' or row_2 == 'o|o|o':
        flag = 1
    elif row_3 == 'x|x|x' or row_3 == 'o|o|o':
        flag = 1
    elif diag_1 == 'x|x|x' or diag_1 == 'o|o|o':
        flag = 1
    elif diag_2 == 'x|x|x' or diag_2 == 'o|o|o':
        flag = 1


while count < 9:
    user_pos = int(input("Enter the position from 1 to 9: "))
    if board[user_pos - 1] == ' ':
        if count % 2 == 0:
            board[user_pos - 1] = 'x'
        else:
            board[user_pos - 1] = 'o'
        print('{}\n{}\n{}'.format(board[:3], board[3:6], board[6:]))
        count += 1
        check_sol()
        if flag == 1:
            print('You have won!')
            break
        if count == 8 and flag == 0:
            print('The match is a draw. Play again.')
    else:
        print('Invalid entry, enter again.')


