from lib.solutions.SUM.sum_solution import SumSolution
import pytest


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_range(self):
        with pytest.raises(Exception, match="Sorry, numbers must be between 0 and 100"):
            SumSolution().compute(-1,101)

    def test_x_value(self):
        with pytest.raises(Exception, match="Sorry, numbers must be between 0 and 100"):
            SumSolution().compute(-1, 99)

    def test_y_value(self):
        with pytest.raises(Exception, match="Sorry, numbers must be between 0 and 100"):
            SumSolution().compute(2, 101)

    def test_boundary_sum(self):
        assert SumSolution().compute(0, 100)


