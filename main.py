from typing import List


class TicTacToe:

    def __init__(self):
        self.top_row: List[str] = [' ', ' ', ' ']
        self.middle_row: List[str] = [' ', ' ', ' ']
        self.bottom_row: List[str] = [' ', ' ', ' ']
        self.horizontal_line = "-" * 9

    def display(self):
        print(" | ".join(self.top_row))
        print(self.horizontal_line)
        print(" | ".join(self.middle_row))
        print(self.horizontal_line)
        print(" | ".join(self.bottom_row))

    def get_position(self):
        position = ""
        valid_row_option = ['T', 'M', 'B']
        valid_col_option = ['L', 'C', 'R']
        while not position:
            position = input("Enter the position [X] to exit (use [TMB][LCR] example MC = [M]iddle [C]enter): ")
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

    def play(self):
        running = True
        is_x_turn = True

        while running:
            self.display()
            symbol = 'X' if is_x_turn else '0'
            position = self.get_position()
            if position == 'X':
                running = False
            else:
                row_position = position[0].upper()
                col_position = position[1].upper()

                row = None
                col = None

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
