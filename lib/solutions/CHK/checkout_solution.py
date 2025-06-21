class CheckoutSolution:

    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
            "F": 10
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
        count_b %= 2
        total += count_b * self.prices["B"]

        #F discount
        if "F" in items:
            count_f = items["F"]
            payable_fs = count_f - (count_f // 3)
            total += payable_fs * self.prices["F"]

        #the rest
        for sku in "CDE":
            total += items.get(sku, 0) * self.prices[sku]

        return total








