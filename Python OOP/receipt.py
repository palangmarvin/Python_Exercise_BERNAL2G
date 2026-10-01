class Receipt:
    def print_receipt(
        self,
        orders,
        subtotal,
        discount,
        total
    ):
        print("\n\n==============================================")
        print("                 CRAVE HUB")
        print("              OFFICIAL RECEIPT")
        print("==============================================")

        print(
            f"{'Item':<20}"
            f"{'Qty':>5}"
            f"{'Price':>10}"
            f"{'Total':>12}"
        )

        print("----------------------------------------------")

        for order in orders:
            print(
                f"{order['name']:<20}"
                f"{order['quantity']:>5}"
                f"₱{order['price']:>9.2f}"
                f"₱{order['total_price']:>11.2f}"
            )

        print("----------------------------------------------")

        print(
            f"{'Subtotal:':<30}"
            f"₱{subtotal:>10.2f}"
        )

        print(
            f"{'Discount:':<30}"
            f"₱{discount:>10.2f}"
        )

        print("----------------------------------------------")

        print(
            f"{'TOTAL:':<30}"
            f"₱{total:>10.2f}"
        )

        print("==============================================")
        print("          Thank you for ordering!")
        print("             Please come again!")
        print("==============================================")