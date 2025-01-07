class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, requested_items, money):
        if requested_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        total_cost = requested_items * self.item_price
        if money < total_cost:
            raise ValueError("Not enough coins")
        self.num_items -= requested_items
        return money - total_cost
