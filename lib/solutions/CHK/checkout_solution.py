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
        for purchased_item, (free_item, offer_qty) in self.free_items.items():
            if purchased_item in items:
                #i.e. 6 // 3 = 2 free items
                if free_item in items:
                    if purchased_item == free_item:
                        size = offer_qty + 1 #how many you actually need to get one free and so
                        free = items[purchased_item] // size
                        items[purchased_item] -= free
                    else:
                        free_qty = items[purchased_item] // offer_qty
                        items[free_item] = max(0, items[free_item] - free_qty)

    #Apply discounted items
    def apply_discount(self, items):
        total = 0

        for sku, count in items.items():
            if sku in self.discount_items:
                for qty, discount_price in sorted(self.discount_items[sku], reverse=True):
                    total += (count // qty) * discount_price
                    count %= qty
            total += count * self.prices[sku]

        return total

    # skus = unicode string
    def checkout(self, skus) -> int:
        items = self.count_items(skus)

        if items == -1:
            return -1
        elif not skus:
            return 0

        self.apply_free_items(items)
        total = self.apply_discount(items)

        return total






