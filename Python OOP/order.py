class Order:
    def __init__(self, menu):
        self.menu = menu
        self.orders = []

    def add_item(self, code, quantity):
        item = self.menu.get_item(code)

        order = {
            "code": code,
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity
        }

        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def display_added_item(self, code, quantity):
        item = self.menu.get_item(code)

        print(
            f"{quantity} x {item['name']} "
            f"added to your order."
        )