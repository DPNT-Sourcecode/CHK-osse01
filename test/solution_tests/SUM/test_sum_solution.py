from lib.solutions.SUM.sum_solution import SumSolution
import pytest


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_negative_int(self):
        with pytest.raises(Exception, match)
