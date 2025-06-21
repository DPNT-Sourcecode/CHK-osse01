from itertools import count


class CheckoutSolution:

    def __init__(self):
        self.prices = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
            "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90,
            "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
            "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90,
            "Y": 10, "Z": 50
        }

        self.free_items = {
            "E": ("B", 2),
            "F": ("F", 2),
            "N": ("M", 3),
            "R": ("Q", 3),
            "U": ("U", 3)
        }

        self.discount_items = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
            "H": [(10, 80), (5, 45)],
            "K": [(2, 150)],
            "P": [(5, 200)],
            "Q": [(3, 80)],
            "V": [(3, 130), (2, 90)]
        }

    #Count
    def count_items(self, skus):
        items = {}

        if not skus:
            return 0

        if not skus.isalpha():
            return -1

        for sku in skus:
            if sku not in self.prices:
                return -1
            # count our items, add one for the first ime
            items[sku] = items.get(sku, 0) + 1

        return items

    #Apply free items first
    def apply_free_items(self, items):
        for purchased_item, (free_item, offer_qty) in self.free_items:
            if purchased_item in items:
                #i.e. 6 // 3 = 2 free items
                free_qty = items[purchased_item] // offer_qty
                if f

    #Apply discounted items

    # skus = unicode string
    def checkout(self, skus) -> int:
        items = self.count_items(skus)


        items = {}

        for sku in skus:
            if sku not in self.prices:
                return -1



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





