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

        items = {}

        for sku in skus:
            if sku not in self.prices:
                return -1

            #count our items, add one for the first ime
            items[sku] = items.get(sku, 0) + 1

        total = 0

        #E discount
        if "E" in items and "B" in items:
            free_bs = items["E"] // 2
            items["B"] = max(0, items["B"] - free_bs)

        #A discount
        count_a = items.get("A", 0)
        total += (count_a // 5) * 200
        count_a %= 5
        total += (count_a // 3) * 130
        count_a %= 3
        total += count_a * self.prices["A"]

        #B discount
        count_b = items.get("B", 0)
        total += (count_b // 2) * 45
        count_b %

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






