from random import randint
board = [' ']*9
global flag
count = 0
flag = 0




def check_sol():

    row_1 = '{}|{}|{}'.format(board[0],board[1],board[2])
    row_2 = '{}|{}|{}'.format(board[3],board[4],board[5])
    row_3 = '{}|{}|{}'.format(board[6],board[7],board[8])
    diag_1 = '{}|{}|{}'.format(board[0],board[4],board[8])
    diag_2 = '{}|{}|{}'.format(board[2],board[4],board[6])
    col_1 = '{}|{}|{}'.format(board[0],board[3], board[6])
    col_2 = '{}|{}|{}'.format(board[1], board[4], board[7])
    col_3 = '{}|{}|{}'.format(board[2], board[5], board[8])

    print(row_1 +'\n'+row_2+'\n'+row_3)

    if(row_1 == 'x|x|x' or row_1 == 'o|o|o'):
        return 1;
    elif(row_2 == 'x|x|x' or row_2 == 'o|o|o'):
        return 1;
    elif(row_3 == 'x|x|x' or row_3 == 'o|o|o'):
        return 1;
    elif(diag_1 == 'x|x|x' or diag_1 == 'o|o|o'):
        return 1;
    elif(diag_2 == 'x|x|x' or diag_2 == 'o|o|o'):
        return 1;
    elif(col_1 == 'x|x|x' or col_1 == 'o|o|o'):
        return 1;
    elif(col_2 == 'x|x|x' or col_2 == 'o|o|o'):
        return 1;
    elif(col_3 == 'x|x|x' or col_3 == 'o|o|o'):
        return 1;
    

# this is user function
def multiplayer():
    global count
    global flag
    while count < 9:
        user_pos = int(input("enter the position from 1 to 9"))
        if board[user_pos - 1] == ' ':
            if count%2 == 0:
                board[user_pos - 1] = 'x'
            else:
                board[user_pos - 1] = 'o'
        
            count = count + 1
            halt = check_sol()
            if(halt == 1):
                print('you have won')
                flag = 1
                break
            if count == 8 and flag == 0:
                print('the match is draw, play again')
        else:
            print('invalid entry, enter again')

# this is AI function
def comp_chance():
        global count
        global flag
        comp_pos = randint(1,9)
        if board[comp_pos - 1] == ' ':
            if count%2 == 0:
                board[comp_pos - 1] = 'x'
            else:
                board[comp_pos - 1] = 'o'
            count = count + 1
            halt = check_sol()
            if(halt == 1):
                print('you have won')
                flag = 1
            if count == 8 and flag == 0:
                print('the match is draw, play again')
        else:
            comp_chance()


def user_chance():
    global count
    global flag
    user_pos = int(input("enter the position from 1 to 9"))
    if board[user_pos - 1] == ' ':
        if count%2 == 0:
            board[user_pos - 1] = 'x'
        else:
            board[user_pos - 1] = 'o'
        
        count = count + 1
        halt = check_sol()
        if(halt == 1):
            print('you have won')
            flag = 1
        if count == 8 and flag == 0:
            print('the match is draw, play again')
    else:
        print('invalid entry, enter again')


print('welcome to the game')
print('there are three modes to the game \n 1. Multiplayer mode \n 2. AI mode \n choose from any of the above')
step_count = 0
temp = int(input())
if temp == 1:
    print('welcome to multiplayer mode')
    multiplayer()
elif temp == 2:
    print('welcome to AI mode')
    while step_count < 9:
        if flag == 1:
            break
        if step_count % 2 == 0:
            user_chance()
        else:
            comp_chance()
        step_count = step_count + 1
        


# board = [' '] * 9
# flag = 0
# count = 0


# def check_sol():
#     row_1 = '{}|{}|{}'.format(board[0], board[1], board[2])
#     row_2 = '{}|{}|{}'.format(board[3], board[4], board[5])
#     row_3 = '{}|{}|{}'.format(board[6], board[7], board[8])
#     diag_1 = '{}|{}|{}'.format(board[0], board[4], board[8])
#     diag_2 = '{}|{}|{}'.format(board[2], board[4], board[6])

#     global flag
#     if row_1 == 'x|x|x' or row_1 == 'o|o|o':
#         flag = 1
#     elif row_2 == 'x|x|x' or row_2 == 'o|o|o':
#         flag = 1
#     elif row_3 == 'x|x|x' or row_3 == 'o|o|o':
#         flag = 1
#     elif diag_1 == 'x|x|x' or diag_1 == 'o|o|o':
#         flag = 1
#     elif diag_2 == 'x|x|x' or diag_2 == 'o|o|o':
#         flag = 1


# while count < 9:
#     user_pos = int(input("Enter the position from 1 to 9: "))
#     if board[user_pos - 1] == ' ':
#         if count % 2 == 0:
#             board[user_pos - 1] = 'x'
#         else:
#             board[user_pos - 1] = 'o'
#         print('{}\n{}\n{}'.format(board[:3], board[3:6], board[6:]))
#         count += 1
#         check_sol()
#         if flag == 1:
#             print('You have won!')
#             break
#         if count == 8 and flag == 0:
#             print('The match is a draw. Play again.')
#     else:
#         print('Invalid entry, enter again.')


