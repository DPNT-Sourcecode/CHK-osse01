from collections import Counter

class CheckoutSolution:

    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40
        }

        self.offers = {
            "A_5_offer": (5, 200),
            "A_3_offer": (3, 130),
            "B": (2, 45)

        }

    # skus = unicode string
    def checkout(self, skus) -> int:
        if not skus:
            return 0

        if not skus.isalpha():
            return -1

        total = 0
        counter = Counter(skus)

        #E offers
        if "E" in counter and "B" in counter:
            free_Bs = counter["E"] // 2
            counter["B"] = max(0, counter["B"] - free_Bs)

        for sku, count in counter.items():
            if sku not in self.prices:
                return -1

            if sku in self.offers:
                qty, new_price = self.offers[sku]
                num_of_offers = count // qty
                remainder = count % qty
                total += num_of_offers * new_price
                total += remainder * self.prices[sku]
            else:
                total += count * self.prices[sku]

        return total







