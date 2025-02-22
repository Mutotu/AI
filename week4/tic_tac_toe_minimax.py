class TicTacToe:
    def __init__(self) -> None:
        # Initialise the game board with empty spaces
        self.__board: [str] = [' ' for _ in range(9)]

    def __display_board(self) -> None:
        """Display the current state of the board."""
        for i in range(0, 9, 3):
            print(f"{self.__board[i]} | {self.__board[i + 1]} | {self.__board[i + 2]}")

    def __player_move(self):
        """Handle the player's move."""
        while True:
            position = int(input("Enter your move (0-8): "))
            if position < 0 or position > 8:
                print("Enter a number between 0-8")
                continue
            if self.__board[position] != ' ':
                print("Position already taken. Try another.")
                continue
            self.__board[position] = 'X'
            break

    def run(self):
        """Main game loop."""
        print("Welcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while True:
            self.__display_board()
            self.__player_move()
            if self.__is_game_end('X'): break
            self.__computer_move()
            if self.__is_game_end('O'): break

    def __is_game_end(self, player):
        """Check if the game has ended either in a win or a draw."""
        if self.__is_winner(player):
            self.__display_board()
            print(f'{player} wins')
            return True
        if self.__is_draw():
            self.__display_board()
            print("It's a draw. Nobody wins")
            return True
        return False

    def __is_draw(self):
        """Check if the game is a draw."""
        for i in self.__board:
            if i == " ": return False
        return True


    def __is_winner(self, player):
        """Check if the given player ("X" or "O") has won the game."""
        board = self.__board
        # check rows
        for i in range(0, 9, 3):
            if player == board[i] == board[i+1] == board[i+2]:
                return True
        # check for columns
        for i in range(3):
            if player == board[i] == board[i+3] == board[i+6]:
                return True
        if player == board[0] == board[4] == board[8] or player == board[2] == board[4] == board[6]:
            return True

        return False

    def __minimax(self, is_maximising):
        """Minimax algorithm to evaluate the best move."""
        if self.__is_winner('O'): return -1  # Computer wins, return -1
        if self.__is_winner('X'): return 1  # Human wins, return +1
        if ' ' not in self.__board: return 0  # Draw, return 0

        if is_maximising:
            best_score = float('-inf')
            for i in range(9):
                if self.__board[i] == " ":
                    self.__board[i] = "X"
                    score = self.__minimax(False)
                    self.__board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.__board[i] == " ":
                    self.__board[i] = "O"
                    score = self.__minimax(True)
                    self.__board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def __computer_move(self):
        """Make a move for the computer using the minimax algorithm."""
        best_score = float('inf')  # The computer (O) minimises
        best_move = None

        for cell in range(len(self.__board)):
            if self.__board[cell] == ' ':
                self.__board[cell] = 'O'
                score = self.__minimax(True)  # Pass True to let the human (X) maximise
                self.__board[cell] = ' '

                if score < best_score:  # Minimising: look for the lowest score
                    best_score = score
                    best_move = cell

        if best_move is not None:
            self.__board[best_move] = 'O'


# Example usage:
if __name__ == "__main__":
    game = TicTacToe()
    game.run()