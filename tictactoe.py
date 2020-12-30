# TIC TAC TOE game
import random
# function to print a tic-tao-toe grid stored as a list of 3 lists
def print_grid(grid):
    for row in grid:
        for e in row:
            print(e, end = ' ')
        print()

# test the function print_grid
grid = [ ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'] ]
empty_cells =[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]


def check_win(grid, player):
    '''function to check if either the user or the computer win the game'''
    result = False
    for i in range(3):
        if grid[i][0]==grid[i][1]==grid[i][2]==player:
            result= True
            break
        elif grid[0][i]==grid[1][i]==grid[2][i]==player :
            result= True
            break
    if (grid[0][0]==grid[1][1]==grid[2][2]==player) or (grid[0][2]==grid[1][1]==grid[2][0]==player):
        result = True
    return result





def get_user_pick(empty_cells, grid):
    ''' function to take a pick from the user who chooses a row and a column'''
    while True :
        print('empty cells:' ,empty_cells)
        x = int(input('Please choose a row: ' ))
        y = int(input('Please choose a column: '))
        if (x,y)in empty_cells:
            grid[x][y]='x'
            empty_cells.remove((x,y))
            print_grid(grid)
            print('*********')
            break
        else :
            print('Sorry this cell is not empty , Choose another one')


# get_user_pick(empty_cells, grid)

def computer_pick(empty_cells, grid):
    '''getting a random choice from the computer'''
    r = random.choice(empty_cells)
    x = r[0]
    y = r[1]
    grid[x][y]='o'
    
    empty_cells.remove((x,y))
    print_grid(grid)
    print('*********')

# computer_pick(empty_cells,grid)
def tictactoe():
    ''' function to play the game 
    '''
    l = ['x','o']
    start = random.choice(l)
    while empty_cells!=[] and check_win(grid,'x')!=True and check_win(grid,'o')!=True: 
        if start == 'x':
            get_user_pick(empty_cells,grid)
            if check_win(grid,'x') or empty_cells==[]:
                break
            if check_win(grid,'o') or empty_cells==[] :
                break
            computer_pick(empty_cells,grid)
            if check_win(grid,'x') or empty_cells==[]:
                break
            if check_win(grid,'o') or empty_cells==[]:
                break
        else:
            computer_pick(empty_cells,grid)
            if check_win(grid,'x') or empty_cells==[]:
                break
            if check_win(grid,'o') or empty_cells==[]:
                break
            get_user_pick(empty_cells,grid)
            if check_win(grid,'x') or empty_cells==[]:
                break
            if check_win(grid,'o') or empty_cells==[]:
                break
            # if empty_cells==[]:
            #     break
    if check_win(grid,'o'):
            print('o won')
    elif check_win(grid,'x'):
            print('x won')
    else:
            print('it is a tie ')

# start the game
tictactoe()

