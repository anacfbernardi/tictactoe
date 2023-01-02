class TicTacToe:
    players = ["X",  "O"]
    winner = None
    current_player = players[0]
    board = [
        '', '', '',
        '', '', '',
        '', '', ''
    ]

    def print_board(self, board):
        """Print the board according the players moves"""

        print(board[0], ' | ', board[1], ' | ', board[2])
        print('----------')
        print(board[3], ' | ', board[4], ' | ', board[5])
        print('----------')
        print(board[6], ' | ', board[7], ' | ', board[8])

    def switch_player(self):
        """Change the player"""

        self.current_player = (self.players[1]
                               if self.current_player == self.players[0]
                               else self.players[0])

    def player_input(self, board):
        """Validate the player input
            and set the position to the player"""

        inp = int(input('enter a position number 1-9: '))
        if 1 <= inp <= 9 and board[inp-1] == '':
            board[inp-1] = self.current_player
            return True

        print('invalid position')
        return False

    def check_horizontale(self, board):
        """Check if there's some horizontal win"""

        for i in range(0, 7, 3):
            if board[i] == board[i+1] == board[i+2] and board[i] != '':
                self.winner = board[i]
                return True
        return False

    def check_vertical(self, board):
        """Check if there's some vertical win"""

        for i in range(0, 3):
            if board[i] == board[i+3] == board[i+6] and board[i] != '':
                self.winner = board[i]
                return True
        return False

    def check_diagonal(self, board):
        """Check if there's some diagonal win"""

        diags = [[0, 4, 8], [2, 4, 6]]
        for position in diags:
            if (board[position[0]] == board[position[1]] == board[position[2]]
                    and board[position[0]] != ''):
                self.winner = board[position[0]]
                return True
        return False

    def check_winner(self, board):
        """Check if there's a winner"""

        if (self.check_horizontale(board)
            or self.check_vertical(board)
                or self.check_diagonal(board)):
            print('Winner is ' + self.winner)

    def check_tie(self, board):
        """Check if the game is a tie"""

        if '' not in board and self.winner is None:
            self.winner = 'tie'
            print('It\'s a tie!')
            return True
        return False

    def check_game(self, board):
        """Check if there's a game result"""

        if self.check_winner(board) or self.check_tie(board):
            self.print_board(board)

    def play_game(self):
        """Play the game!"""
        board = self.board.copy()

        while self.winner is None:
            self.print_board(board)
            while self.player_input(board) is False:
                self.print_board(board)
            self.switch_player()
            self.check_game(board)
