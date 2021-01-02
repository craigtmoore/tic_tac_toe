from typing import List, Dict


class TicTacToe:

    def __init__(self):
        self.positions: Dict[str, str] = dict()

        self.valid_row_option = ['T', 'M', 'B']
        self.valid_col_option = ['L', 'C', 'R']
        for row in self.valid_row_option:
            for col in self.valid_col_option:
                self.positions[f"{row}{col}"] = " "

        self.horizontal_line = "-" * 11 + " " + "-" * 14

    def display(self):
        for row_name in self.valid_row_option:
            row = []
            for col in self.valid_col_option:
                row.append(self.positions[f"{row_name}{col}"])
            self.print_row(row, row_name)
            if row_name != self.valid_row_option[2]:
                print(self.horizontal_line)

    def print_row(self, row : List[str], row_name: str):
        print(" " + " | ".join(row) + "   " + " | ".join((row_name + x for x in self.valid_col_option)))

    def get_position(self):
        position = ""
        while not position:
            position = input("Enter the position [X] to exit (use [TMB][LCR] example MC = [M]iddle [C]enter): ").upper()
            if position == 'X':
                return position

            if len(position) < 2:
                position = ""

            if position[0] not in self.valid_row_option:
                position = ""
                print(f"The first letter must be {self.valid_row_option}")

            if position[1] not in self.valid_col_option:
                position = ""
                print(f"The second letter must be {self.valid_col_option}")

        return position

    def determine_row_winner(self, row: str) -> str:
        first = self.positions[f"{row}{self.valid_col_option[0]}"]
        second = self.positions[f"{row}{self.valid_col_option[1]}"]
        third = self.positions[f"{row}{self.valid_col_option[2]}"]
        if first == second == third != " ":
            return f"'{first}' wins! (column win)"
        return ''

    def determine_col_winner(self, col: str) -> str:
        first = self.positions[f"{self.valid_row_option[0]}{col}"]
        second = self.positions[f"{self.valid_row_option[1]}{col}"]
        third = self.positions[f"{self.valid_row_option[2]}{col}"]
        if first == second == third != " ":
            return f"'{first}' wins! (column win)"
        return ''

    def determine_diagonal_winner(self):
        first = self.positions[f"{self.valid_row_option[0]}{self.valid_col_option[0]}"]
        second = self.positions[f"{self.valid_row_option[1]}{self.valid_col_option[1]}"]
        third = self.positions[f"{self.valid_row_option[2]}{self.valid_col_option[2]}"]
        if first == second == third != " ":
            return f"'{first}' wins! (diagonal left-to-right)"
        first = self.positions[f"{self.valid_row_option[0]}{self.valid_col_option[2]}"]
        second = self.positions[f"{self.valid_row_option[1]}{self.valid_col_option[1]}"]
        third = self.positions[f"{self.valid_row_option[2]}{self.valid_col_option[0]}"]
        if first == second == third != " ":
            return f"'{first}' wins! (diagonal right-to-left)"
        return ''

    def determine_winner(self) -> str:
        for row in self.valid_row_option:
            winner = self.determine_row_winner(row)
            if winner:
                return winner
        for col in self.valid_col_option:
            winner = self.determine_col_winner(col)
            if winner:
                return winner
        # Determine Diagonal Winner
        winner = self.determine_diagonal_winner()
        if winner:
            return winner
        return ""

    def play(self):
        running = True
        is_x_turn = True

        while running:
            self.display()
            winner = self.determine_winner()
            if winner:
                print(winner)
                play_again = input('Play again [Y] or [N]? ').upper()
                if len(play_again) == 0 or play_again[0] == 'N':
                    running = False
            else:
                symbol = 'X' if is_x_turn else '0'
                position = self.get_position().upper()
                if position == 'X':
                    running = False
                else:
                    self.positions[position] = symbol
                    is_x_turn = not is_x_turn


if __name__ == '__main__':
    TicTacToe().play()
