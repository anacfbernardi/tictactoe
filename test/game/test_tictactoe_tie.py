from game.tictactoe import TicTacToe
from pathlib import Path
from unittest import mock
import sys

directory = Path(__file__).absolute()
sys.path.append(str(directory.parent.parent))


class TestTicTacToeTie:

    def run_test_with_inputs_and_get_output(self, capfd, inputs):
        game = TicTacToe()

        with mock.patch('builtins.input', side_effect=inputs):
            game.play_game()

        out, err = capfd.readouterr()
        return out

    def test_TicTacToe_whenTie_shouldReturnTieMessage(self, capfd):
        inputs = ['1', '2', '3', '5', '6', '7', '4', '9', '8']
        out = self.run_test_with_inputs_and_get_output(capfd, inputs)
        assert "It's a tie!" in out
