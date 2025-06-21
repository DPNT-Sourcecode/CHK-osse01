from lib.solutions.SUM.sum_solution import SumSolution
import pytest


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_range(self):
        with pytest.raises(Exception, match="Sorry, number must be between 0 and 100"):
            SumSolution().compute(1,99)


