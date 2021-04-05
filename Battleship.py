##
##=======================================================
## Jaskirat Pabla
## Game of Battleship
##=======================================================
##


import check


## Data Definitions:

## Deployments is a (listof (listof Nat))
## Requires:
##   The length of the outer list is 5.
##   The length of the first inner list is 5.
##   The length of the second inner list is 4.
##   The length of the third inner list is 3.
##   The length of the fourth inner list is 3.
##   The length of the fifth inner list is 2.

## A Board is a (listof (listof Str))
## Requires:
##   The length of the outer list is 10.
##   The length of each inner list is 10.
##   Each string is '.', 'C', 'B', 'D', 'S', or 'P'.


## Global Constants:
input_prompt = "Enter a guess: "
invalid_text = "You must enter a number between 1 and 100!"
hit_msg = "Hit!"
miss_msg = "Miss!"
game_over_msg = "Game Over!"
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def empty_board():
    '''
    Returns a list of lists representing a Battleship
    board where each entry is a period.
    
    empty_board: None -> Board
    '''
    dot = '.'
    empty_board_lol = []
    while (len(empty_board_lol) != 10):
        row = dot * 10
        row = list(row)
        empty_board_lol.append(row)
    return empty_board_lol


def flat_lst(lol):
    '''
    Returns a list of integers contaning all of the integers
    in each of the inner lists in lol.
    
    flat_lst: (listof (listof Nat)) -> (listof Nat)
    '''
    new_lst = []
    for row in lol:
        for column in row:
            new_lst.append(column)
    return new_lst


def mutate_board(num, letter, game_board):
    '''
    Mutates game_board so that position num in game_board is
    replaced with letter.

    Effects: Mutates game_board.

    mutate_board: Nat (anyof 'C' 'B' 'D' 'S' 'P') Board -> None
    Requires: 0 < num < 101
    '''
    tens = num // 10
    ones = num % 10
    if ((num % 10) == 0):
        column = 9
        row = tens - 1
    else:
        column = ones - 1
        row = tens
    game_board[row][column] = letter


def board_set_up(lol, battleship_board):
    '''
    Mutates battleship_board so that each position in battleship_board
    is mutated to 'C', 'B', 'D', 'S', or 'P' in the position that they
    appear in lol, otherwise the position remains as '.'.

    Effects: Mutates battleship_board.

    board_set_up: Deployments Board -> None
    Requires: None of the inner lists of lol can share the
              same numbers, and
              Every number in the inner lists of lol must be
              between 1 and 100 (inclusive).
    '''
    for pos in lol[0]:
        mutate_board(pos, 'C', battleship_board)
    for pos in lol[1]:
        mutate_board(pos, 'B', battleship_board)
    for pos in lol[2]:
        mutate_board(pos, 'D', battleship_board)
    for pos in lol[3]:
        mutate_board(pos, 'S', battleship_board)
    for pos in lol[4]:
        mutate_board(pos, 'P', battleship_board)


def valid_checker(string_num):
    '''
    Returns True if string_num is a string that represents a natural
    number between 1 and 100 (inclusive), and returns False otherwise.

    valid_checker: Str -> Bool
    '''
    truth = string_num.isdigit()
    if (truth == True):
        integer = int(string_num)
        if (integer < 1):
            truth = False
        elif (integer > 100):
            truth = False
    return truth


def valid_looper():
    '''
    Returns the value read from keyboard if input is an integer between
    1 and 100 (inclusive), otherwise prints invalid_text and loops
    until an integer between 1 and 100 (inclusive) is inputted.

    Effects: Reads input from keyboard.
             Prints to the screen.

    valid_guess: None -> Nat
    '''
    guess = input(input_prompt)
    is_valid = valid_checker(guess)
    while (is_valid != True):
        print(invalid_text)
        guess = input(input_prompt)
        is_valid = valid_checker(guess)
    guess = int(guess)
    return guess


def flat_board(battleship_board):
    '''
    Prints battleship_board line-by-line with no string or list symbols.

    Effects: Prints to the screen.

    flat_board: Board -> None
    '''
    for row in battleship_board:
        line = ' '.join(row)
        print(line)


def battleship(deployments):
    '''
    Consumes a nested list deployments and returns number of valid
    guesses made. Prints hit_msg if user sinks ship, miss_msg if no ship
    is hit, invalid_text if invalid guess is made, and game_over_msg once
    all ships are sunken and finally the game board is printed.

    Effects:
        Reads input from keyboard.
        Prints to the screen.

    battleship: Deployments -> Nat
    Requires: None of the inner lists of deployments can share the
              same numbers, and
              Every number in the inner lists of deployments must be
              between 1 and 100 (inclusive).
    
    Examples:
        If L = [[1, 2, 3, 4, 5], [6, 7, 8, 9],
                [10, 11, 12], [13, 14, 15], [16, 17]] then
        battleship(L) => 17 and the following interactions are
        inputted and printed:
        >>> Enter a guess: 1
        Hit!
        >>> Enter a guess: 2
        Hit!
        >>> Enter a guess: 3
        Hit!
        >>> Enter a guess: 4
        Hit!
        >>> Enter a guess: 5
        Hit!
        >>> Enter a guess: 6
        Hit!
        >>> Enter a guess: 7
        Hit!
        >>> Enter a guess: 8
        Hit!
        >>> Enter a guess: 9
        Hit!
        >>> Enter a guess: 10
        Hit!
        >>> Enter a guess: 11
        Hit!
        >>> Enter a guess: 12
        Hit!
        >>> Enter a guess: 13
        Hit!
        >>> Enter a guess: 14
        Hit!
        >>> Enter a guess: 15
        Hit!
        >>> Enter a guess: 16
        Hit!
        >>> Enter a guess: 17
        Hit!
        Game Over!
        . . . . . . . . . D
        . . . . . . . . . D
        . . . . . P P . . D
        . . . . . . . . . .
        . B . . . . . . . .
        . B . . S S S . . .
        . B . . . . . . . .
        . B . . . . . . . .
        . . . . . . . . . .
        . . . . . C C C C C

        If L = [[96, 97, 98, 99, 100],[42, 52, 62, 72],
                [10, 20, 30],[55, 56, 57],[26, 27]] then
        battleship(L) => 20 and the following interactions are
        inputted and printed:
        >>> Enter a guess: 96
        Hit!
        >>> Enter a guess: 95
        Miss!
        >>> Enter a guess: 97
        Hit!
        >>> Enter a guess: melon
        You must enter a number beteween 1 and 100. 
        >>> Enter a guess: 98
        Hit!
        >>> Enter a guess: 99
        Hit!
        >>> Enter a guess: 100
        Hit!
        >>> Enter a guess: 42
        Hit!
        >>> Enter a guess: 52
        Hit!
        >>> Enter a guess: 62
        Hit!
        >>> Enter a guess: 72
        Hit!
        >>> Enter a guess: 9
        Miss!
        >>> Enter a guess: 10
        Hit!
        >>> Enter a guess: 20
        Hit!
        >>> Enter a guess: 30
        Hit!
        >>> Enter a guess: 55
        Hit!
        >>> Enter a guess: 56
        Hit!
        >>> Enter a guess: 57
        Hit!
        >>> Enter a guess: 25
        Miss!
        >>> Enter a guess: 26
        Hit!
        >>> Enter a guess: 27
        Hit!
        Game Over!
        . . . . . . . . . D
        . . . . . . . . . D
        . . . . . P P . . D
        . . . . . . . . . .
        . B . . . . . . . .
        . B . . S S S . . .
        . B . . . . . . . .
        . B . . . . . . . .
        . . . . . . . . . .
        . . . . . C C C C C
    '''
    valid_guess = 0
    final_lst = []
    battle_board = empty_board()
    flat_deployments = flat_lst(deployments)
    board_set_up(deployments, battle_board)
    while ((len(final_lst)) != (len(flat_deployments))):
        posn = valid_looper()
        if posn in flat_deployments:
            if ((posn in final_lst) == False):
                final_lst.append(posn)
            print(hit_msg)
        else:
            print(miss_msg)
        valid_guess += 1
    print(game_over_msg)
    flat_board(battle_board)
    return valid_guess


## Examples:
L = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17]]
check.set_input('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                '11', '12', '13', '14', '15', '16', '17')
check.set_print_exact(hit_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      hit_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      hit_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      hit_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      hit_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      hit_msg+'\n'+hit_msg+'\n' + \
                      game_over_msg+'\n' + \
                      'C C C C C B B B B D\n' \
                      'D D S S S P P . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . . . . . .')
check.expect("Ex 1 - Small Numbers, all are hits", battleship(L), 17)

L = [[96, 97, 98, 99, 100],[42, 52, 62, 72], [10, 20, 30],[55, 56, 57],
     [26, 27]]
check.set_input('96', '95', '97', 'melon', '98', '99', '100', '42',
                '52', '62', '72', '9', '10', '20', '30', '55', '56',
                '57', '25', '26', '27')
check.set_print_exact(hit_msg+'\n'+miss_msg+'\n'+hit_msg+'\n'+
                      invalid_text+'\n'+hit_msg+'\n'+hit_msg+'\n'+ \
                      hit_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      hit_msg+'\n'+hit_msg+'\n'+miss_msg+'\n' + \
                      hit_msg+'\n'+hit_msg+'\n'+hit_msg + \
                      '\n'+hit_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      miss_msg+'\n'+hit_msg+'\n'+hit_msg+'\n' + \
                      game_over_msg+'\n' + \
                      '. . . . . . . . . D\n' \
                      '. . . . . . . . . D\n' \
                      '. . . . . P P . . D\n' \
                      '. . . . . . . . . .\n' \
                      '. B . . . . . . . .\n' \
                      '. B . . S S S . . .\n' \
                      '. B . . . . . . . .\n' \
                      '. B . . . . . . . .\n' \
                      '. . . . . . . . . .\n' \
                      '. . . . . C C C C C')
check.expect("Ex 2 - typical", battleship(L), 20)


## Test:
L = [[10, 20, 30, 40, 50],[60, 70, 80, 90], [100, 99, 98],[1, 2, 3],
     [55, 45]]
check.set_input('96', '95', '96', '95', '96', '95', '96', '95',
                'y', 'n', 'y', 'n', 'y', 'n', 'y', 'n', 'y', 'n',
                '10', '60', '100', '1', '55', '45', '2', '3', '99',
                '98', '70', '80', '90', '50', '40', '20', '30')
check.set_print_exact((miss_msg+'\n') * 8 + \
                      (invalid_text+'\n') * 10 + \
                      (hit_msg+'\n') * 17 + \
                      game_over_msg+'\n' + \
                      'S S S . . . . . . C\n' \
                      '. . . . . . . . . C\n' \
                      '. . . . . . . . . C\n' \
                      '. . . . . . . . . C\n' \
                      '. . . . P . . . . C\n' \
                      '. . . . P . . . . B\n' \
                      '. . . . . . . . . B\n' \
                      '. . . . . . . . . B\n' \
                      '. . . . . . . . . B\n' \
                      '. . . . . . . D D D')
check.expect("Test 1 - lots of misses and invalid guesses",
             battleship(L), 25)
