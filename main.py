def show_intro():
    """
    Prints out an introduction to the game with instructions on how to play
    """
    pass


def no_winner() -> bool:
    """
    Verify that there is no winner on the board

    :return: true if there is no winner, false otherwise
    """
    return False


def init_board():
    """
    Initializes the game board
    """
    pass


def show_board():
    """
    Displays the game board
    """
    pass


def ask_choice():
    """
    Asks for the position of the next player on the board. Will verify the position before allowing the player to
    place their piece. Additionally the player can choose to end the game as well.
    """
    pass


def show_outro():
    """
    Show a message declaring either a winner or a draw
    """
    pass


def switch_player():
    """
    Switch the current player
    """
    pass


if __name__ == '__main__':
    player = 'o'
    board = [[]]

    show_intro()
    init_board()
    while no_winner():
        switch_player()
        show_board()
        ask_choice()
    show_outro()
