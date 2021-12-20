"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['BOT', 'JOT', 'LIT', 'PEEP'], 'SIN')
    False
    """
    value = False
    if word in wordlist:
        value = True
    return value


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'C', 'C', 'G'], ['N', 'S', 'A', 'P']], 1)
    'NSAP'
    >>> make_str_from_row([['A', 'Q', 'U', 'I', 'T'], ['A', 'N', 'T', 'S', 'Y']], 0)
    'AQUIT'
    """
    new_str = ''
    for s in board[row_index]:
        new_str = new_str + s
    return new_str


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'V', 'Q', 'P', 'R'], ['B', 'P', 'D', 'C', 'X']], 3)
    'PC'
    >>> make_str_from_column([['V', 'I', 'K', 'T', 'O', 'R'], ['N', 'I', 'C', 'K', 'I', 'E'], ['B', 'R', 'A', 'N', 'D', 'Y']], 3)
    'TKN'
    """
    new_str = ''
    for i in range(len(board)):
        new_str = new_str + board[i][column_index]
    return new_str


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word_in_row([['T', 'A', 'X', 'I'], ['T', 'M', 'A', 'X']], 'AXE')
    False
    >>> board_contains_word_in_row([['P', 'O', 'O', 'R', 'S'], ['P', 'W', 'O', 'Q', 'M']], 'OR')
    True
    """
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True
    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'X', 'M', 'T'], ['T', 'W', 'E', 'O']], 'ME')
    True
    >>> board_contains_word_in_column([['A', 'X', 'M', 'T'], ['T', 'W', 'E', 'O'], ['E', 'A', 'L', 'R']], 'ATE')
    True
    """
    for i in range(len(board[0])):
        if word in make_str_from_column(board, i):
            return True
    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['T', 'A', 'X', 'I'], ['O', 'M', 'I', 'F']], 'IF')
    True
    >>> board_contains_word([['T', 'A', 'X', 'I'], ['O', 'M', 'I', 'F']], 'TAXI')
    True
    >>> board_contains_word([['M', 'A', 'T', 'H'], ['C', 'O', 'I', 'N'], ['W', 'G', 'N', 'Y']], 'FOUR')
    False
    """
    if board_contains_word_in_column(board, word) or board_contains_word_in_row(board, word):
        return True
    return False


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('SCORE')
    5
    >>> word_score('CHARACTERS')
    30
    """
    count = len(word)
    if count < 3:
        score = 0
    elif count in [3,4,5,6]:
        score = count
    elif count in [7,8,9]:
        score = 2 * count
    else:
        score = 3 * count
    return score



def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    player_info[1] = player_info[1] + word_score(word)
    return


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    >>> num_words_on_board([['B', 'A', 'T', 'L'], ['S', 'U', 'N', 'T']], ['BAT', 'AT', 'SUN', 'BATTLE'])
    3
    >>> num_words_on_board([['D', 'O', 'N', 'I', 'T'], ['J', 'U', 'S', 'T', 'O']], ['JUST', 'DO', 'IT', 'TO', 'DON', 'SIN'])
    5
    """
    count = 0
    for i in range(len(words)):
        if board_contains_word(board, words[i]):
            count = count + 1
    return count



def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    words = []
    lines = words_file.readlines()
    for i in range(len(lines)):
        words.append(lines[i].rstrip('\n'))        
    return words


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    
    Return a list of strings where strings have length 1
    """
    lines = board_file.readlines()
    board = [[] for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != '\n':
                board[i].append(lines[i][j])
    return board
