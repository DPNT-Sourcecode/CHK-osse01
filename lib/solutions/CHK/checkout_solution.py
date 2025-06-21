from collections import Counter

class CheckoutSolution:

    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }

        self.offers = {
            "A": (3, 130),
            "B": (2, 45)
        }

    # skus = unicode string
    def checkout(self, skus) -> int:
        if not skus.isalpha():
            return -1

        total = 0
        counter = Counter(skus)

        for skus, count in counter.items():






