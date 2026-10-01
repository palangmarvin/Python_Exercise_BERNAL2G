from menu import display_menu
from order import get_yes_no, create_order
from billing import calculate_bill
from receipt import print_receipt


def display_welcome():
    print("==============================================")
    print("          WELCOME TO CRAVE HUB!")
    print("==============================================")


def main():

    display_welcome()

    display_menu()

    if not get_yes_no(
        "\nWould you like to place an order? (Yes/No): "
    ):
        print("\nThank you for visiting Crave Hub!")
        print("Have a great day!")
        return

    orders = create_order()

    subtotal, discount, total = calculate_bill(orders)

    print_receipt(
        orders,
        subtotal,
        discount,
        total
    )


if __name__ == "__main__":
    main()