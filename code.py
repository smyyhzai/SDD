
import random
import os
import time

#os.system('cls')

# this function prints the grid of the city


def print_grid(x):
    os.system('cls')
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
    print('     ', end='')
    for i in range(x-1):
        print(letters[i], end='   ')
    print(letters[x-1])
    count = 0
    row = 0
    for count in range(1, x+1):
        print('   ' + '+---'*x + '+')
        if count < 10:
            print('{}'.format(count), end='  ')
            for i in range(x):
                print('|{:^3}'.format(grid[row][i]), end='')
                                                                                                                                                        
        else:
            print('{}'.format(count), end=' ')
            for i in range(x):
                print('|{:^3}'.format(grid[row][i]), end='')
        print('|')
        row = row + 1
    # print bottom row
    print('   ' + '+---'*x + '+')


# this function displays the game options
def game(highScores):
    build_choice = 1
    global turn
    global coin


    while build_choice != '0':
        if coin != 1:
            turn = turn + 1
            coin = coin - 1
            #print_grid(grid_size)
            first_building = random.choice(building)
            second_building = random.choice(building)
            # ensure that first_building and second_building is not the same
            while first_building == second_building:
                if first_building == second_building:
                    second_building = random.choice(building)

            if first_building == 'R':
                first_building_name = 'Residential (R)'
            elif first_building == 'I':
                first_building_name = 'Industry (I)   '
            elif first_building == 'C':
                first_building_name = 'Commercial (C) '
            elif first_building == 'O':
                first_building_name = 'Park (O)       '
            elif first_building == '*':
                first_building_name = 'Road (*)       '

            if second_building == 'R':
                second_building_name = 'Residential (R)'
            elif second_building == 'I':
                second_building_name = 'Industry (I)   '
            elif second_building == 'C':
                second_building_name = 'Commercial (C) '
            elif second_building == 'O':
                second_building_name = 'Park (O)       '
            elif second_building == '*':
                second_building_name = 'Road (*)       '

            total_score = current_score()


            print(' ______________________________________________ ')
            print("|     Turn: {}      Point: {}     Coin: {}       |".format(turn, total_score, coin))
            print('|----------------------------------------------|')
            print('| Options:                                     |')
            print('|  1. Build a {}                  |'.format(first_building_name)     )
            print('|  2. Build a {}                  |'.format(second_building_name)     )
            print('|                                              |')
            print('|  3. Save game                                |')
            print('|  4. See score breakdown                      |')
            print('|  0. Exit to main menu                        |')
            print('|  00. Exit game                               |')
            print('|______________________________________________|')
            print()
            build_choice = (input('Your choice? '))


            # first building choice
            if build_choice == '1':
                build_buildings(first_building)
            # second building choice
            elif build_choice == '2':
                build_buildings(second_building)
            # save game
            elif build_choice == '3':
                os.system('cls')
                turn = turn - 1
                coin = coin + 1
                save_game(turn)
                print('Game saved!')
                break
            # see current score
            elif build_choice == '4':
                os.system('cls')
                turn = turn - 1
                coin = coin + 1
                enter = ''
                print_score(total_score, res_scores, ind_scores, com_scores, par_scores, rod_scores)
                enter = (input('Click enter to resume game.'))
                os.system('cls')
                print_grid(grid_size)
            # exit to menu
            elif build_choice == '0':
                os.system('cls')
                break
            elif build_choice == '00':
                os.system('cls')
                print('Goodbye, see you again')
                exit()
            else:
                validation_failed()
            # turn = turn - 1 ensure that turn number doesn't change if input is not valid
        else:
            # turn has reached 16, show final layout
            end_of_game(grid, highScores)
            build_choice = '0'


# this function performs the necessary actions if the validation failed
def validation_failed():
    global turn
    global coin
    turn = turn - 1
    coin = coin + 1
    #os.system('cls')
    print_grid(grid_size)
    print('Invalid input, please try again.\n')



# this function validates the building input and build the building accordingly
def build_buildings(building_choice):

    valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    global turn
    global coin
    global row
    global col
    global grid_size
    result = True

    # for player to input where they are building at
    build = input('Build where? ').upper()

    # validation for if build input is empty
    if build == '':
        validation_failed()
        result = False

    # validation for if there is no 2nd character in build input
    elif len(build) == 1:
        validation_failed()
        result = False

    # validation for if 2nd character is not a number in build input
    elif not build[1].isnumeric():
        validation_failed()
        result = False

    # validation for if number is not a valid number
    elif build[1] not in valid_numbers:
        validation_failed()
        result = False

    # validation if build input has more than 3 characters
    elif len(build) > 3:
        validation_failed()
        result = False

    # check col number of input
    else:
        letter = build[0]
        if letter == 'A':
            col_number = 0
        elif letter == 'B':
            col_number = 1
        elif letter == 'C':
            col_number = 2
        elif letter == 'D':
            col_number = 3
        elif letter == 'E':
            col_number = 4
        elif letter == 'F':
            col_number = 5
        elif letter == 'G':
            col_number = 6
        elif letter == 'H':
            col_number = 7
        elif letter == 'I':
            col_number = 8
        elif letter == 'J':
            col_number = 9
        elif letter == 'K':
            col_number = 10
        elif letter == 'L':
            col_number = 11
        elif letter == 'M':
            col_number = 12
        elif letter == 'N':
            col_number = 13
        elif letter == 'O':
            col_number = 14
        elif letter == 'P':
            col_number = 15
        elif letter == 'Q':
            col_number = 16
        elif letter == 'R':
            col_number = 17
        elif letter == 'S':
            col_number = 18
        elif letter == 'T':
            col_number = 19
        else:
            validation_failed()
            result = False

    # validation passed, check where the building is supposed to be placed
    if result == True:
        row_number = int(build[1:])
        row_number = row_number - 1
        # allow to put freely on turn 1
        if turn == 1:
            grid[row_number][col_number] = building_choice
            print_grid(grid_size)
        # turn 2 onwards must build orthogonally adjacent to a building
        else:
            up_row = row_number - 1
            up_col = col_number

            down_row = row_number + 1
            down_col = col_number

            left_row = row_number
            left_col = col_number - 1

            right_row = row_number
            right_col = col_number + 1

            # check if cell has building already
            if grid[row_number][col_number] != '   ':
                print_grid(grid_size)
                print('There is already a building at {}\n'.format(build))
                turn = turn - 1
                coin = coin + 1
            else:
                # able to build
                if up_row >= 0 and grid[up_row][up_col] != '   ':
                    grid[row_number][col_number] = building_choice
                    print_grid(grid_size)
                elif down_row <= 19 and grid[down_row][down_col] != '   ':
                    grid[row_number][col_number] = building_choice
                    print_grid(grid_size)
                elif left_col >= 0 and grid[left_row][left_col] != '   ':
                    grid[row_number][col_number] = building_choice
                    print_grid(grid_size)
                elif right_col <= 19 and grid[right_row][right_col] != '   ':
                    grid[row_number][col_number] = building_choice
                    print_grid(grid_size)
                else:
                    print('You must build next to existing building\n')
                    turn = turn - 1
                    coin = coin + 1

        row = row_number
        col = col_number


# this is a function to check the number of buildings left after every turn
def remainding_buildings(grid):
    # number of each buildings at the start
    hse = 8
    fac = 8
    shp = 8
    hwy = 8
    bch = 8
    for i in range(0, 4):
        for x in range(0, 4):

            if grid[i][x] == 'R':
                coin = coin - 1
            elif grid[i][x] == 'I':
                coin = coin - 1
            elif grid[i][x] == 'C':
                coin = coin - 1
            elif grid[i][x] == 'O':
                coin = coin - 1
            elif grid[i][x] == '*':
                coin = coin - 1

    print('Building           Remaining')
    print('--------           ---------')
    print('HSE                ', hse)
    print('FAC                ', fac)
    print('SHP                ', shp)
    print('HWY                ', hwy)
    print('BCH                ', bch)



# this is a function that checks for adjacency for side buildings
def check_four_directions():
    top = ''
    bottom = ''
    left = ''
    right = ''
    global row
    global col

    if row != 0:
        top = grid[row - 1][col]
    if row != 19:
        bottom = grid[row + 1][col]
    if col != 0:
        left = grid[row][col - 1]
    if col != 19:
        right = grid[row][col + 1]

    return top, bottom, left, right


# this is a function to check BCH scores
def calc_bch_score(bch_scores, col):
    # if its is in col A or D then 3 points
    if col == 0 or col == 20:
        bch_scores.append(3)
    # base point is 1
    else:
        bch_scores.append(1)
    


# this is a function to check FAC scores
def calc_fac_scores(fac_scores, fac):
    for i in range(fac):
        # add score into list
        # count < 4, first 4 will be based on how many FAC are there
        if fac <= 4:
            fac_scores.append(fac)
        # count > 4, first 4 is 4 points
        elif fac > 4:
            fac_scores.append(4)
            fac_scores.append(4)
            fac_scores.append(4)
            fac_scores.append(4)
            fac = fac - 4
            # subsequent FAC is 1 point
            for x in range(fac):
                fac_scores.append(1)
            break


# this is a function to check hse scores
def calc_hse_score(hse_scores, row, col):
    # count of number of adjacent HSE or SHP
    num_of_hse_shp = 0
    # count of number of adjacent BCH
    num_of_bch = 0
    # checks for adjacency for side buildings
    top, bottom, left, right = check_four_directions(row, col)

    if left == 'FAC' or right == 'FAC':
        hse_scores.append(1)  # add score into list
    else:
        # check top
        if top == 'HSE' or top == 'SHP':
            # 1 point when cell is HSE or SHP
            num_of_hse_shp = num_of_hse_shp + 1
        elif top == 'BCH':
            # 2 point when cell is BCH
            num_of_bch = num_of_bch + 2

        # check bottom
        if bottom == 'HSE' or bottom == 'SHP':
            num_of_hse_shp = num_of_hse_shp + 1
        elif bottom == 'BCH':
            num_of_bch = num_of_bch + 2

        # check right
        if right == 'HSE' or right == 'SHP':
            num_of_hse_shp = num_of_hse_shp + 1
        elif right == 'BCH':
            num_of_bch = num_of_bch + 2

        # check left
        if left == 'HSE' or left == 'SHP':
            num_of_hse_shp = num_of_hse_shp + 1
        elif left == 'BCH':
            num_of_bch = num_of_bch + 2

        # add score into list
        hse_scores.append(num_of_hse_shp+num_of_bch)


# this is a function to check shp scores
def calc_shp_score(shp_scores, row, col):
    building_seen = []
    # checks for adjacency for side buildings
    top, bottom, left, right = check_four_directions(row, col)
    # add 1 point for every unique building adjacent to the SHP
    if building_seen.count(left) == 0:
        building_seen.append(left)
    if building_seen.count(right) == 0:
        building_seen.append(right)
    if building_seen.count(top) == 0:
        building_seen.append(top)
    if building_seen.count(bottom) == 0:
        building_seen.append(bottom)
    # remove errors that occured
    if building_seen.count('   ') > 0:
        building_seen.remove('   ')
    if building_seen.count('') > 0:
        building_seen.remove('')
    # add score into list
    shp_scores.append(len(building_seen))


# this is a function to check hwy scores
def calc_hwy_score(hwy_scores, row, col):
    # count 1 when a HWY is seen
    hwy_count = 1
    # check towards the right side for the row for any HWYs
    for i in range(3 - col):
        next_cell = grid[row][col + i + 1]
        if next_cell == 'HWY':
            hwy_count = hwy_count + 1
        else:
            break
    # check towards the left side for the row for any HWYs
    for i in range(col):
        next_cell = grid[row][col - i - 1]
        if next_cell == 'HWY':
            hwy_count = hwy_count + 1
        else:
            break
    # add score into list
    hwy_scores.append(hwy_count)

# this is a function to check industry scores
def calc_ind_score(ind_scores):
    global row
    global col
    global coin
    ind_count = 0
    # checks for adjacency for side buildings
    top, bottom, left, right = check_four_directions()
        # add coins
    # add 1 point for every res building adjacent to it
    if top == "R":
        coin = coin + 1
    if bottom == "R":
        coin = coin + 1
    if left == "R":
        coin = coin + 1
    if right == "R":
        coin = coin + 1
    for row in range(0, 20):
        for col in range(0, 20):
            cell = grid[row][col]
            if cell == 'I':
                ind_count = ind_count + 1
    ind_scores.clear()
    ind_scores.append(ind_count)
    

            


# this is a function to check commerical scores
def calc_com_score(com_scores):
    global row
    global col
    global coin
    com_counts = 0
    # checks for adjacency for side buildings
    top, bottom, left, right = check_four_directions()
    # add 1 point for every unique building adjacent to the park
    if top == "C":
        com_counts = com_counts + 1
    if bottom == "C":
        com_counts = com_counts + 1
    if left == "C":
        com_counts = com_counts + 1
    if right == "C":
        com_counts = com_counts + 1
   
    if com_counts != 0:
        # add score into list
        com_scores.append(com_counts)

    # add coins
    if top == "R":
        coin = coin + 1
    if bottom == "R":
        coin = coin + 1
    if left == "R":
        coin = coin + 1
    if right == "R":
        coin = coin + 1
    

# this is a function to check rod scores
# 1 point per connected road


def calc_rod_score(rod_scores):
    global row
    global col
    rod_count = 0
    # check towards the right side
    for i in range(19 - col):
        next_cell = grid[row][col + i + 1]
        if next_cell == '*':
            rod_count = rod_count + 1
        else:
            break
    # check towards the left side
    for i in range(col):
        next_cell = grid[row][col - i - 1]
        if next_cell == '*':
            rod_count = rod_count + 1
        else:
            break
    if rod_count != 0:
        # add score into list
        rod_scores.append(rod_count)

# this is a function to check residential scores


def calc_res_score(res_scores):
    top, bottom, left, right = check_four_directions()
    global row
    global col
    res_counts = 0
    if top == "I" or bottom == "I" or left == "I" or right == "I":
        res_counts += 1
    else:
        # check top for R or C
        if top == "R" or top == "C":
            res_counts += 1
        if top == "O":
            res_counts += 2

        if bottom == "R" or bottom == "C":
            res_counts += 1
        if bottom == "O":
            res_counts += 2

        if left == "R" or left == "C":
            res_counts += 1
        if left == "O":
            res_counts += 2

        if right == "R" or right == "C":
            res_counts += 1
        if right == "O":
            res_counts += 2

    if res_counts != 0:
        # add to score list
        res_scores.append(res_counts)
    

def calc_par_score(par_scores):
    par_counts = 0
    global row
    global col
    # checks for adjacency for side buildings
    top, bottom, left, right = check_four_directions()
    # add 1 point for every unique building adjacent to the park
    if top == "O":
        par_counts = par_counts + 1
    if bottom == "O":
        par_counts = par_counts + 1
    if left == "O":
        par_counts = par_counts + 1
    if right == "O":
        par_counts = par_counts + 1
   
    if par_counts != 0:
        # add score into list
        par_scores.append(par_counts)
    

# this is a function to display scores for all buildings


def display_scores(building_scores, cell):
    output = ''
    # if there is a score for the building, show workings and tabulate total score
    if len(building_scores) == 1:
        print('{}: '.format(
            cell) + str(sum(building_scores)))
    elif len(building_scores) > 0:
        for i in range(1, len(building_scores)):
            output = output + ' + ' + str(building_scores[i])
        print('{}: '.format(
            cell) + str(building_scores[0]) + output + ' = ' + str(sum(building_scores)))
    # if there is no score for the building
    else:
        print('{}: 0 '.format(cell))


# this is a function to check the current score for every building
def current_score():
    bch_scores = []
    fac_scores = []
    hse_scores = []
    shp_scores = []
    hwy_scores = []

    fac = 0
    global row
    global col
    # access the grid with the row and col
    cell = grid[row][col]


    # to check if grid has C
    if cell == 'C':
        calc_com_score(com_scores)

            # to check if grid has *
    if cell == '*':
        calc_rod_score(rod_scores)

            # to check if grid has R
    if cell == 'R':
        calc_res_score(res_scores)

            # to check if grid has O
    if cell == 'O':
        calc_par_score(par_scores)

            # to check if grid has I
    if cell == 'I':
        calc_ind_score(ind_scores)

    # FAC scores needs to be calculated from the number of FACs
    calc_fac_scores(fac_scores, fac)
    row = -1
    col = -1

    # total score
    total_score = sum(res_scores + ind_scores + com_scores + par_scores + rod_scores)

    return total_score

def print_score(total_score, res_scores, ind_scores, com_scores, par_scores, rod_scores):
    # display scores
    print()
    print('Score breakdown')
    print('---------------')


    # R scores
    display_scores(res_scores, 'Residential')

    # I scores
    display_scores(ind_scores, 'Industry')

    # C scores
    display_scores(com_scores, 'Commercial')

    # O scores
    display_scores(par_scores, 'Park')

    # * scores
    display_scores(rod_scores, 'Road')

    # total score
    total_score = sum(res_scores + ind_scores + com_scores + par_scores + rod_scores)
    print()
    print('Total score:', str(total_score))

# this is a function to save the game into SimpCity txt file
def save_game(turn):
    datafile = open('SimpCity.txt', 'w')
    datafile.write(str(turn) + '\n')
    datafile.write(str(coin) + '\n')
    for row in range(0, 20):
        data = ''
        for col in range(0, 20):
            data = data + grid[row][col] + ','
        datafile.write(data + '\n')
    datafile.close()


# this is a function to read game from SimpCity txt file
def load_game():
    global turn
    global coin
    # check if file is available
    datafile = open('SimpCity.txt', 'a')
    datafile.close()

    # read game from file
    datafile = open('SimpCity.txt', 'r')
    turn = int(datafile.readline())
    coin = int(datafile.readline())
    row = 0
    for line in datafile:
        line = line.strip('\n')
        datalist = line.split(',')
        for col in range(0, 20):
            grid[row][col] = datalist[col]
        row = row+1
    datafile.close()


# this is a function to save scores to HighScore txt file
def save_high_scores(highScores):
    datafile = open('HighScores.txt', 'w')
    for i in range(len(highScores)):
        player = highScores[i]
        datafile.write(player[0] + ',' + str(player[1])+'\n')
    datafile.close()


# this is a function to read high score from HighScores file
def load_high_scores():
    scores = []

    # check if file is available
    datafile = open('HighScores.txt', 'a')
    datafile.close()

    # read high scores from file
    datafile = open('HighScores.txt', 'r')
    for line in datafile:
        line = line.strip('\n')
        score_list = line.split(',')
        scores.append(score_list)

    for i in range(len(scores)):
        scores[i][1] = int(scores[i][1])

    datafile.close()
    return scores


# this is a function to show the end of game
def end_of_game(grid, highScores):
    pos = 1
    total_score = current_score()
    print_score(total_score, res_scores, ind_scores, com_scores, par_scores, rod_scores)
    for player in highScores:
        if player[1] >= total_score:
            pos = pos + 1
        else:
            break

    # in highscore board
    if pos < 10:
        print('Congratulations! You made the high score board at position {}!'.format(pos))
        name = input('Please enter your name (max 20 chars): ')
        while len(name) > 20:
            print('You have exceeded to max characters')
            name = input('Please enter your name (max 20 chars): ')
        new_player = []
        # add player to list
        new_player.append(name)
        # add player's score to list
        new_player.append(total_score)
        # add player and score into position in highscore board
        highScores.insert(pos-1, new_player)
        if len(highScores) == 11:
            highScores.remove(highScores[-1])
        # save new high scores
        save_high_scores(highScores)
        # show high scores
        display_high_scores(highScores)
        enter = (input('Click enter to return to main menu.'))
        os.system('cls')


    else:
        print('Your score is ', total_score)


# this function will show the highest scores of up to 10 players
# with the name and the score for the player in desc order
def display_high_scores(scores):

    print()
    print('--------- HIGH SCORES ---------')
    print('Pos Player                Score')
    print('--- ------                -----')
    for i in range(len(scores)):
        print('{:>2}. {:<25}{}'.format(i + 1, scores[i][0], scores[i][1]))
    print('-------------------------------')
    print()

def help():
    print('How to Play')
    print('-----------')
    print('•This city-building game begins with 16 coins.')
    print('•In each turn, the player will construct one of two randomly-selected buildings in the 20x20 city.')
    print('•Each construction cost 1 coin.')
    print('•For the first building, the player can build anywhere in the city.')
    print('•For subsequent constructions, the player can only build on squares that are connected to existing buildings.')
    print('•The other building that was not built is discarded.')
    print('The game will end when the player runs out of coins.')
    print()
    print('Scoring system')
    print('--------------')
    print('Each building scores in a different way.') 
    print('The objective of the game is to build a city that scores as many points as possible.')
    print('There are 5 types of buildings:')
    print('•Residential (R): If it is next to an industry (I), then it scores 1 point only.')
    print('  Otherwise, it scores 1 point for each adjacent residential (R) or commercial (C),')
    print('  and 2 points for each adjacent park (O).')
    print('•Industry (I): Scores 1 point per industry in the city.')
    print('  Each industry generates 1 coin per residential building adjacent to it.')
    print('•Commercial (C): Scores 1 point per commercial adjacent to it.')
    print('  Each commercial generates 1 coin per residential adjacent to it.')
    print('•Park (O): Scores 1 point per park adjacent to it.')
    print('•Road (*): Scores 1 point per connected road (*) in the same row.')
    print()

def settings():
    global grid_size
    os.system('cls')
    print('Settings')
    print('--------')
    print('1. Grid Size')
    print()
    print('0. Exit')
    while True:
        choice = (input('Choose option: '))     
        if choice == '1':
            os.system('cls')
            print('Please choose the grid size for the game.')
            print('1. 5x5')
            print('2. 10x10')
            print('3. 15x15')
            print('4. 20x20')
            print()
            print('0. Back')
            while True:
                option = (input('Choose grid size: '))
                if option == '1':
                    grid_size = 5
                    break
                elif option == '2':
                    grid_size = 10
                    break
                elif option == '3':
                    grid_size = 15
                    break
                elif option == '4':
                    grid_size = 20
                    break
                elif option == '0':
                    break
                else:
                    print('Invalid option! Please try again.\n')
                    continue
            if option == '1' or option == '2' or option == '3' or option == '4':
                os.system('cls')
                print('Grid size updated to {}x{}!'.format(grid_size,grid_size))
                break
            else:
                continue
            
        elif choice == '0':
            break
        else:
            print('Invalid option! Please try again.\n')
            continue

# main program

# global variables
building = ['O', 'C', 'I', '*', 'R']
grid = [
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
        '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
        '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
        '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
        '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
     '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
]
com_scores = []
rod_scores = []
res_scores = []
par_scores = []
ind_scores = []


highScores = load_high_scores()
turn = 0
row = -1
col = -1
grid_size = 20
# main menu
os.system('cls')
choice = 1
while choice != '0':

    #print('Welcome to Ngee Ann City!')
    #print('-------------------------')
    print(r"""
   _  __               ___               ______ __      
  / |/ /__ ____ ___   / _ | ___  ___    / ___(_) /___ __
 /    / _ `/ -_) -_) / __ |/ _ \/ _ \  / /__/ / __/ // /
/_/|_/\_, /\__/\__/ /_/ |_/_//_/_//_/  \___/_/\__/\_, / 
     /___/                                       /___/  
    """)
    print(' ___________________________________ ')
    print('| x             Menu                |')
    print('|-----------------------------------|')
    print('| 1. Start new game                 |')
    print('| 2. Load saved game                |')
    print('| 3. Show high scores               |')
    print('| 4. Help                           |')
    print('| 5. Settings                       |')
    print('|                                   |')
    print('| 0. Exit                           |')
    print('|___________________________________|')
    print()
    choice = (input('Your choice? '))

    if choice == '1':
        # reset turn when game restart
        turn = 0
        coin = 17
        # reset grid when game restart
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                grid[row][col] = '   '

        print_grid(grid_size)
        game(highScores)
    elif choice == '2':
        try:
            load_game()
            print_grid(grid_size)
            game(highScores)
        # to ensure that there is a saved game txt file
        except ValueError:
            print('No saved game found. Please start a new game.')
            time.sleep(3)
    elif choice == '3':
        enter = ''
        os.system('cls')
        display_high_scores(highScores)
        enter = (input('Click enter to resume game.'))
        os.system('cls')
    elif choice == '4':
        os.system('cls')
        help()
        enter = (input('Click enter to return to main menu.'))
        os.system('cls')
    elif choice == '5':
        os.system('cls')
        settings()
    elif choice == '0':
        os.system('cls')
        print('Goodbye, see you again')
    else:
        os.system('cls')
        print('Invalid option, please try again')