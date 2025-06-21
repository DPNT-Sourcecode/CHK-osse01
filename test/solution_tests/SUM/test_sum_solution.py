from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_negatve_int(self):
        assert SumSolution().compute(-1, 3) == None