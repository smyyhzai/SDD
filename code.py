
import random


# this function prints the grid of the city


def print_grid():
    print('     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T  ')
    count = 0
    row = 0
    for count in range(1, 21):
        print('   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')
        if count < 10:
            print('{}  |{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|'.format(count, grid[row][0], grid[row][1], grid[row][2], grid[row][3], grid[row][4], grid[row][5], grid[row][6], grid[row][7], grid[row]
                                                                                                                                                         [8], grid[row][9], grid[row][10], grid[row][11], grid[row][12], grid[row][13], grid[row][14], grid[row][15], grid[row][16], grid[row][17], grid[row][18], grid[row][19]))
        else:
            print('{} |{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|'.format(count, grid[row][0], grid[row][1], grid[row][2], grid[row][3], grid[row][4], grid[row][5], grid[row][6], grid[row][7], grid[row]
                                                                                                                                                        [8], grid[row][9], grid[row][10], grid[row][11], grid[row][12], grid[row][13], grid[row][14], grid[row][15], grid[row][16], grid[row][17], grid[row][18], grid[row][19]))
        row = row + 1
    # print bottom row
    print('   +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+')


# this function displays the game options
def game(highScores):
    build_choice = 1
    global turn
    global coin

    if choice != '2':
        global total_score
        global coin
        # reset turn when game restart
        turn = 0
        coin = 17
        # reset grid when game restart
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                grid[row][col] = '   '

    while build_choice != '0':
        
        if coin != 1:
            global total_score
            current_score(total_score)
            turn = turn + 1
            coin = 17 - turn 
            #print_grid()
            first_building = random.choice(building)
            second_building = random.choice(building)
            # ensure that first_building and second_building is not the same
            while first_building == second_building:
                if first_building == second_building:
                    second_building = random.choice(building)

            if first_building == 'R':
                first_building_name = 'Residential (R)'
            elif first_building == 'I':
                first_building_name = 'Industry (I)'
            elif first_building == 'C':
                first_building_name = 'Commercial (C)'
            elif first_building == 'O':
                first_building_name = 'Park (O)'
            elif first_building == '*':
                first_building_name = 'Road (*)'

            if second_building == 'R':
                second_building_name = 'Residential (R)'
            elif second_building == 'I':
                second_building_name = 'Industry (I)'
            elif second_building == 'C':
                second_building_name = 'Commercial (C)'
            elif second_building == 'O':
                second_building_name = 'Park (O)'
            elif second_building == '*':
                second_building_name = 'Road (*)'


            #total_score = current_score()
            print()
            print("Turn: {}    Point: {}   Coin: {} ".format(turn, total_score, coin))
            print()
            print("Options:")
            print('--------')
            print('1. Build a', first_building_name)
            print('2. Build a', second_building_name)
            print()
            print('3. Save game')
            print('4. Show score breakdown')
            print('0. Exit to main menu')
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
                turn = turn - 1
                save_game(turn)
                print('Game saved!')
                break
            elif build_choice == '4':
                print_current_score()
            # exit game
            elif build_choice == '0':
                break
            else:
                turn = turn - 1
                print('Invalid input, please try again.\n')
            # turn = turn - 1 ensure that turn number doesn't change if input is not valid
        else:
            # turn has reached 16, show final layout
            end_of_game(grid, highScores)
            build_choice = '0'


# this function performs the necessary actions if the validation failed
def validation_failed():
    global turn
    turn = turn - 1
    print('Invalid input, please try again.\n')


# this function validates the building input and build the building accordingly
def build_buildings(building_choice):

    valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    global turn
    global coin
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
            print('6')

    # validation passed, check where the building is supposed to be placed
    if result == True:
        row_number = int(build[1:])
        row_number = row_number - 1
        # allow to put freely on turn 1
        if turn == 1:
            grid[row_number][col_number] = building_choice
            print_grid()
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
                print('There is already a building at {}\n'.format(build))
                turn = turn - 1
            # able to build
            if up_row >= 0 and grid[up_row][up_col] != '   ':
                grid[row_number][col_number] = building_choice
                print_grid()
            elif down_row <= 19 and grid[down_row][down_col] != '   ':
                grid[row_number][col_number] = building_choice
                print_grid()
            elif left_col >= 0 and grid[left_row][left_col] != '   ':
                grid[row_number][col_number] = building_choice
                print_grid()
            elif right_col <= 19 and grid[right_row][right_col] != '   ':
                grid[row_number][col_number] = building_choice
                print_grid()
            else:
                print('You must build next to existing building\n')
                turn = turn - 1


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
def check_four_directions(row, col):
    top = ''
    bottom = ''
    left = ''
    right = ''

    if row != 0:
        top = grid[row - 1][col]
    if row != 3:
        bottom = grid[row + 1][col]
    if col != 0:
        left = grid[row][col - 1]
    if col != 3:
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


# this is a function to check hwy scores // commercial
def calc_com_score(com_scores, row, col):
    """top, bottom, left, right = check_four_directions(row, col)
    com_count = 0
    if top == "C" or bottom == "C" or left == "C" or right == "C":
        com_count += 1"""
    # count 1 when a commercial (C) is seen
    com_count = 0
    # check towards the right side for the row for any Cs
    for i in range(19 - col):
        next_cell = grid[row][col + i + 1]
        if next_cell == 'C':
            com_count = com_count + 1
        else:
            break
    # check towards the left side for the row for any Cs
    for i in range(col):
        next_cell = grid[row][col - i - 1]
        if next_cell == 'C':
            com_count = com_count + 1
        else:
            break
    # add score into list
    com_scores.append(com_count)


# this is a function to check rod scores
# 1 point per connected road


def calc_rod_score(rod_scores, row, col):
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
    # add score into list
    rod_scores.append(rod_count)

# this is a function to check residential scores


def calc_res_score(res_scores, row, col):
    top, bottom, left, right = check_four_directions(row, col)
    res_counts = 0
    if top == "I" or bottom == "I" or left == "I" or right == "I":
        res_counts += 1
    else:
        # check top for R or C
        if top == "R" or top == "C":
            res_counts += 1
        elif top == "O":
            res_counts += 2

        if bottom == "R" or bottom == "C":
            res_counts += 1
        elif bottom == "O":
            res_counts += 2

        if left == "R" or left == "C":
            res_counts += 1
        elif left == "O":
            res_counts += 2

        if right == "R" or right == "C":
            res_counts += 1
        elif right == "O":
            res_counts += 2
    # add to score list
    res_scores.append(res_counts)

def calc_par_score(par_scores, row, col):
    par_counts = 0
    # checks for adjacency for side buildings
    top, bottom, left, right = check_four_directions(row, col)
    # add 1 point for every unique building adjacent to the park
    if top == "O":
        par_counts += 1
    if bottom == "O":
        par_counts += 1
    if left == "O":
        par_counts += 1
    if right == "O":
        par_counts += 1
   
    # add score into list
    par_scores.append(par_counts)

# this is a function to display scores for all buildings


def display_scores(building_scores, cell):
    output = ''
    # if there is a score for the building, show workings and tabulate total score
    if len(building_scores) > 0:
        for i in range(1, len(building_scores)):
            output = output + ' + ' + str(building_scores[i])
        print('{}: '.format(
            cell) + str(building_scores[0]) + output + ' = ' + str(sum(building_scores)))
    # if there is no score for the building
    else:
        print('{}: 0 '.format(cell))


# this is a function to check the current score for every building
def current_score(total_scores):

    fac = 0
    global total_score

    # access the grid with the row and col
    for row in range(0, 20):
        for col in range(0, 20):
            # save whatever is that is on the grid for the row and col into cell
            cell = grid[row][col]

            # to check if grid has BCH
            if cell == "BCH":
                calc_bch_score(bch_scores, col)

            # to check if grid has FAC
            if cell == 'FAC':
                fac = fac + 1

            # to check if grid has HSE
            if cell == 'HSE':
                calc_hse_score(hse_scores, row, col)

            # to check if grid has SHP
            if cell == 'SHP':
                calc_shp_score(shp_scores, row, col)

            # to check if grid has C
            if cell == 'C':
                calc_com_score(com_scores, row, col)

            # to check if grid has *
            if cell == '*':
                calc_rod_score(rod_scores, row, col)

            # to check if grid has R
            if cell == 'R':
                calc_res_score(res_scores, row, col)

            # to check if grid has O
            if cell == 'O':
                calc_par_score(par_scores, row, col)

    # FAC scores needs to be calculated from the number of FACs
    calc_fac_scores(fac_scores, fac)

    # total score
    total_score = sum(com_scores + rod_scores + res_scores + par_scores)


    return total_score

def print_current_score():
    current_score(total_score)
    # display scores
    print()

    # C scores
    display_scores(com_scores, 'Commercial')

    # * scores
    display_scores(rod_scores, 'Road')

    # R scores
    display_scores(res_scores, 'Residential')

    # O scores
    display_scores(par_scores, 'Park')

    # total score
    print('Total score:', str(total_score))
    print()


# this is a function to save the game into SimpCity txt file
def save_game(turn):
    datafile = open('SimpCity.txt', 'w')
    datafile.write(str(turn) + '\n')
    for row in range(len(grid)):
        data = ''
        for col in range(len(grid[row])):
            data = data + grid[row][col] + ','
        datafile.write(data + '\n')
    datafile.close()

# this is a function to read game from SimpCity txt file
def load_game():
    global turn
    # check if file is available
    datafile = open('SimpCity.txt', 'a')
    datafile.close()

    # read game from file
    datafile = open('SimpCity.txt', 'r')
    turn = int(datafile.readline())
    row = 0
    for line in datafile:
        line = line.strip('\n')
        datalist = line.split(',')
        for col in range(len(grid[row])):
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

    print_current_score()

    global total_score

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

highScores = load_high_scores()
turn = 0
bch_scores = []
fac_scores = []
hse_scores = []
shp_scores = []
com_scores = []
rod_scores = []
res_scores = []
par_scores = []

# main menu
print('Welcome to Ngee Ann City!')
print('-------------------------')
choice = 1
while choice != '0':
    print()
    print('1. Start new game')
    print('2. Load saved game')
    print('3. Show high scores')
    print()
    print('0. Exit')
    choice = (input('Your choice? '))

    if choice == '1':
        total_score = 0
        print_grid()
        game(highScores)
    elif choice == '2':
        try:
            load_game()
            print_grid()
            game(highScores)
        # to ensure that there is a saved game txt file
        except ValueError:
            print('No saved game found')
    elif choice == '3':
        display_high_scores(highScores)
    elif choice == '0':
        print('Goodbye, see you again')
    else:
        print('Invalid option, please try again')
