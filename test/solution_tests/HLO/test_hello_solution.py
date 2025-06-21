from lib.solutions.HLO.hello_solution import HelloSolution

class TestHelloSolution:
    def test_msg(self):
        hello_msg = HelloSolution()
        assert hello_msg.hello("Sam") == "Hello, World!"