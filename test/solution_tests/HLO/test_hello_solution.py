from lib.solutions.HLO.hello_solution import HelloSolution

class TestHelloSolution:
    def test_msg(self):
        hello_msg = HelloSolution()
        assert hello_msg.hello("John") == "Hello, John!"

    def test_not_null(self):
        hello_msg = HelloSolution()
        assert hello_msg.hello("John") is not None