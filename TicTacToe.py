import random

count = 0

def display(grid):
    print()
    print("   0 1 2")
    print("   _ _ _")
    y = 0
    for i in grid:
        i = str(grid[y])
        i = i.replace("' '","_")
        i = i.replace("'x'","x")
        i = i.replace("'o'","o")
        i = i.replace(",","|")      
        i = i.replace(" ","")       
        i = i.replace("["," |")
        i = i.replace("]","|")
        i = str(y)+i
        print(i)
        y += 1
        
#field input
def infield(player):
    global logo
    global count
    logo = player
    display(grid)
    if count == 9:
                raise SystemExit("It's a tie -- nobody wins..")
    else:
        while True:
                arg = logo
                try:
                    row = int(input("Player: {0}! Please enter your desired row number: ".format(arg)))
                    col = int(input("Player: {0}! Please enter your desired column number: ".format(arg)))
                except ValueError:
                    print("Row and Column must be a number. Try again!") 
                    continue
                if row in range(0,3) and col in range(0,3): 
                            if grid[int(row)][int(col)] != ' ':
                                print("Field already taken. Please try again!")
                                continue
                            else:
                                #update grid + count
                                grid[row][col] = logo
                                count = count+ 1
                                break
                else:
                    print('Column/Row must be a number in the range of 0-2. Please try again!')
                    continue 


#function to check for win
def check(player):
    logo = player
    if (
                                    (grid[0][0]== logo and grid[0][1]== logo and grid[0][2] == logo) or 
                                    (grid[0][0]== logo and grid[1][0]== logo and grid[2][0] == logo) or 
                                    (grid[0][0]== logo and grid[1][1]== logo and grid[2][2] == logo) or 
                                    (grid[1][0]== logo and grid[1][1]== logo and grid[1][2] == logo) or
                                    (grid[2][0]== logo and grid[2][1]== logo and grid[2][2] == logo) or
                                    (grid[0][1]== logo and grid[1][1]== logo and grid[2][1] == logo) or
                                    (grid[0][2]== logo and grid[1][2]== logo and grid[2][2] == logo) or
                                    (grid[2][0]== logo and grid[1][1]== logo and grid[0][2] == logo)
                                    ):
                                    display(grid)

                                    k = '!!'
                                    for i in range(0,25):
                                        j = '!!'
                                        print(k)
                                        k += j
                                    raise SystemExit("Player "+logo+" wins!")    

grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


#player input to choose symbol

lst = []
while True:
    symbol = input("Player 1: Please choose your symbol (x or o):")
    if symbol != 'x' and symbol != 'o':
            print("Your symbol must be x or o! Try again!")
            continue
    else:
            lst.append(symbol)
            break
    

while True:    
    symbol2 = input("Player 2: Please choose your symbol (x or o):")
    if symbol2 != 'x' and symbol2 != 'o':
            print("Your symbol must be x or o! Try again!")
            continue
    elif symbol2 == symbol:
            print("Sorry symbol already taken. Choose another!")
            continue
    
    else:
            lst.append(symbol2)
            break

random.shuffle(lst)  

#actual game

input("Please press enter to start the game!")
arg = lst[0]
print()
print("Player {0} starts!!!".format(arg))
print()


while True:
    player = lst[0]
    infield(player)
    check(player)    
    player = lst[1]
    infield(player)
    check(player)
