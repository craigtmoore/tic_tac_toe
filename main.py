from typing import List


class TicTacToe:

    def __init__(self):
        self.top_row: List[str] = [' ', ' ', ' ']
        self.middle_row: List[str] = [' ', ' ', ' ']
        self.bottom_row: List[str] = [' ', ' ', ' ']
        self.horizontal_line = "-" * 11 + " " + "-" * 14

    def display(self):
        self.print_row(self.top_row, "T")
        print(self.horizontal_line)
        self.print_row(self.middle_row, "M")
        print(self.horizontal_line)
        self.print_row(self.bottom_row, "B")

    def print_row(self, row, row_name):
        print(" " + " | ".join(row) + "   " + " | ".join((row_name + x for x in ["L", "C", "R"])))

    def get_position(self):
        position = ""
        valid_row_option = ['T', 'M', 'B']
        valid_col_option = ['L', 'C', 'R']
        while not position:
            position = input("Enter the position [X] to exit (use [TMB][LCR] example MC = [M]iddle [C]enter): ").upper()
            if position == 'X':
                return position

            if len(position) < 2:
                position = ""

            if position[0] not in valid_row_option:
                position = ""
                print(f"The first letter must be {valid_row_option}")

            if position[1] not in valid_col_option:
                position = ""
                print(f"The second letter must be {valid_col_option}")

        return position

    def determine_row_winner(self, row: List[str]):
        if row[0] == row[1] == row[2] != " ":
            print(f"'{row[0]}' wins! (row win)")
            return True
        return False

    def determine_col_winner(self, col: int):
        if self.top_row[col] == self.middle_row[col] == self.bottom_row[col] != " ":
            print(f"'{self.top_row[col]}' wins! (column win)")
            return True
        return False

    def determine_winner(self):
        found_winner = False
        for row in [self.top_row, self.middle_row, self.bottom_row]:
            if self.determine_row_winner(row):
                return True
        for col in [0, 1, 2]:
            if self.determine_col_winner(col):
                return True
        # Determine Diagonal Winner
        if self.top_row[0] == self.middle_row[1] == self.bottom_row[2] != " ":
            print(f"'{self.top_row[0]}' wins! (right-to-left diagonal)")
            return True
        if self.top_row[2] == self.middle_row[1] == self.bottom_row[0] != " ":
            print(f"'{self.top_row[2]}' wins! (left-to-right diagonal)")
            return True
        return False

    def play(self):
        running = True
        is_x_turn = True

        while running:
            self.display()
            if self.determine_winner():
                running = False
            else:
                symbol = 'X' if is_x_turn else '0'
                position = self.get_position().upper()
                if position == 'X':
                    running = False
                else:
                    row_position = position[0].upper()
                    col_position = position[1].upper()

                    row = None

                    if row_position == 'T':
                        row = self.top_row
                    elif row_position == 'M':
                        row = self.middle_row
                    elif row_position == 'B':
                        row = self.bottom_row

                    if col_position == 'L':
                        row[0] = symbol
                    elif col_position == 'C':
                        row[1] = symbol
                    elif col_position == 'R':
                        row[2] = symbol

                    is_x_turn = not is_x_turn


if __name__ == '__main__':
    TicTacToe().play()
