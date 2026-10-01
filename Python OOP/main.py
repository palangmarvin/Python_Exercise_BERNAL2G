from menu import Menu
from order import Order
from billing import Billing
from receipt import Receipt


def display_welcome():
    print("==============================================")
    print("          WELCOME TO CRAVE HUB!")
    print("==============================================")


def get_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer == "yes" or answer == "y":
            return True

        elif answer == "no" or answer == "n":
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
            print(
                "Invalid quantity. "
                "Please enter a whole number."
            )


def get_order(menu, order):
    while True:

        code = input(
            "\nEnter menu code: "
        ).strip().upper()

        if not menu.has_item(code):
            print(
                "Invalid menu code. "
                "Please choose from the menu."
            )
            continue

        quantity = get_quantity()

        order.add_item(code, quantity)

        order.display_added_item(code, quantity)

        if not get_yes_no(
            "\nDo you want to order another item? (Yes/No): "
        ):
            break


def main():

    menu = Menu()
    order = Order(menu)
    billing = Billing()
    receipt = Receipt()

    display_welcome()
    menu.display_menu()

    if not get_yes_no(
        "\nWould you like to place an order? (Yes/No): "
    ):
        print("\nThank you for visiting Crave Hub!")
        print("Have a great day!")
        return

    get_order(menu, order)

    orders = order.get_orders()

    subtotal, discount, total = (
        billing.calculate_total(orders)
    )

    receipt.print_receipt(
        orders,
        subtotal,
        discount,
        total
    )


if __name__ == "__main__":
    main()