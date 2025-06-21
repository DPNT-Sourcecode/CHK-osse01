
class SumSolution:
    
    def compute(self, x, y):
        if not (0 <= x <= 100) or not (0 <= y <= 100):
            raise Exception("Sorry, numbers must be between 0 and 100")
        return x + y
