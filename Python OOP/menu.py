class Menu:
    def __init__(self):
        self.items = {
            "B1": {"name": "Classic Burger", "price": 85.00},
            "B2": {"name": "Cheese Burger", "price": 95.00},
            "B3": {"name": "Chicken Sandwich", "price": 105.00},
            "F1": {"name": "French Fries", "price": 55.00},
            "F2": {"name": "Chicken Nuggets", "price": 75.00},
            "M1": {"name": "Spaghetti Meal", "price": 120.00},
            "D1": {"name": "Iced Tea", "price": 45.00},
            "D2": {"name": "Soft Drink", "price": 40.00},
            "D3": {"name": "Bottled Water", "price": 30.00}
        }

    def display_menu(self):
        print("==============================================")
        print("                 CRAVE HUB")
        print("                 FULL MENU")
        print("----------------------------------------------")
        print(f"{'Code':<8}{'Menu Item':<25}{'Price':>10}")

        for code, item in self.items.items():
            print(
                f"{code:<8}"
                f"{item['name']:<25}"
                f"₱{item['price']:>8.2f}"
            )

        print("==============================================")

    def get_item(self, code):
        return self.items.get(code)

    def has_item(self, code):
        return code in self.items