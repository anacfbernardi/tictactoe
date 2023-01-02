from game.tictactoe import TicTacToe
from pathlib import Path
from unittest import mock
import sys
from pytest import CaptureFixture

directory = Path(__file__).absolute()
sys.path.append(str(directory.parent.parent))


class TestTicTacToeDiagonals:
    x_winner_message = "Winner is X"

    def run_test_with_inputs_and_get_output(self, capfd, inputs): 
        game = TicTacToe()

        with mock.patch('builtins.input', side_effect=inputs):
            game.play_game()

        out, err = capfd.readouterr()
        return out

    def test_TicTacToe_whenDiagonal0_winnerIsX_shouldReturnTieMessage(self, capfd):
        """ The game:
             X  |  O  |  
            ----------
                |  X  |
            ----------
                |  O  | X
        """
        inputs = ['1', '2', '5', '8',  '9']
        out = self.run_test_with_inputs_and_get_output(capfd, inputs)
        assert self.x_winner_message in out

    def test_TicTacToe_whenDiagonal1_winnerIsX_shouldReturnTieMessage(self, capfd):
        """ The game:
                |     |  X
            ----------
             O  |  X  |  O
            ----------
             X  |     |
        """

        inputs = ['3', '4', '5', '6',  '7']
        out = self.run_test_with_inputs_and_get_output(capfd, inputs)
        assert self.x_winner_message in out
