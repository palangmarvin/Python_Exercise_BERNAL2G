class Billing:
    def calculate_subtotal(self, orders):
        subtotal = 0

        for order in orders:
            total_price = (
                order["price"] * order["quantity"]
            )

            order["total_price"] = total_price
            subtotal += total_price

        return subtotal

    def calculate_discount(self, subtotal):
        if subtotal >= 500:
            return subtotal * 0.10

        return 0

    def calculate_total(self, orders):
        subtotal = self.calculate_subtotal(orders)

        discount = self.calculate_discount(subtotal)

        total = subtotal - discount

        return subtotal, discount, total