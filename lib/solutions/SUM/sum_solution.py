
class SumSolution:
    
    def compute(self, x, y):
        if not (0 <= x <= 100) or (0 <= y <= 100):
            raise Exception("Sorry, number must be between 0 and 100")
        return x + y
