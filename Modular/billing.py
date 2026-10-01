def calculate_item_total(order):
    return order["price"] * order["quantity"]


def calculate_subtotal(orders):
    subtotal = 0

    for order in orders:
        order["total_price"] = calculate_item_total(order)
        subtotal += order["total_price"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= 500:
        return subtotal * 0.10

    return 0


def calculate_total(subtotal, discount):
    return subtotal - discount


def calculate_bill(orders):
    subtotal = calculate_subtotal(orders)
    discount = calculate_discount(subtotal)
    total = calculate_total(subtotal, discount)

    return subtotal, discount, total