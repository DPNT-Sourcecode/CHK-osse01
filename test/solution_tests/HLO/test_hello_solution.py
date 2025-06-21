from lib.solutions.HLO.hello_solution import HelloSolution

class TestHello():
    def test_msg(self):
        assert HelloSolution.hello("Sam") == "hello to the world"