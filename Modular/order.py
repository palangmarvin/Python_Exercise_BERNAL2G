from menu import MENU


def get_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer in ["yes", "y"]:
            return True

        elif answer in ["no", "n"]:
            return False

        else:
            print("Invalid input. Please enter Yes or No.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")


def get_item_code():
    while True:
        item_code = input("\nEnter menu code: ").strip().upper()

        if item_code in MENU:
            return item_code

        print("Invalid menu code. Please choose from the menu.")


def create_order():
    orders = []

    while True:
        item_code = get_item_code()
        quantity = get_quantity()

        item = MENU[item_code]

        order = {
            "code": item_code,
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity
        }

        orders.append(order)

        print(
            f"{quantity} x {item['name']} "
            f"added to your order."
        )

        if not get_yes_no(
            "\nDo you want to order another item? (Yes/No): "
        ):
            break

    return orders