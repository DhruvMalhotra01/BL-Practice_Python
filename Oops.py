from abc import ABC, abstractmethod


# Discount System

class Discount(ABC):

    @abstractmethod
    def calculate(self, total):
        """Return price after applying discount"""
        pass


class RegularPrice(Discount):

    def calculate(self, total):
        return total


class FlatPercentageOff(Discount):

    def __init__(self, rate):
        if rate < 0 or rate > 100:
            raise ValueError("Discount must be between 0 and 100.")
        self.rate = rate

    def calculate(self, total):
        discount_amount = total * self.rate / 100
        return total - discount_amount


# Item

class Item:

    def __init__(self, title, cost):
        self.title = title
        self.cost = cost

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, amount):
        if amount <= 0:
            raise ValueError("Item cost must be greater than zero.")
        self._cost = amount

    def __str__(self):
        return f"{self.title} (₹{self.cost:.2f})"


#Shopping Order

class ShoppingOrder:

    def __init__(self, order_number, discount=None):
        self.order_number = order_number
        self.products = []
        self.discount = discount #or RegularPrice()

    def add(self, item):
        if not isinstance(item, Item):
            raise TypeError("Only Item objects can be added.")
        self.products.append(item)

    def subtotal(self):
        return sum(product.cost for product in self.products)

    def final_amount(self):
        return self.discount.calculate(self.subtotal())

    # Dunder Methods

    def __len__(self):
        return len(self.products)

    def __getitem__(self, position):
        return self.products[position]

    def __str__(self):
        product_details = "\n".join(
            f"{i}. {product}"
            for i, product in enumerate(self.products, start=1)
        )

        return (
            f"\n===== ORDER #{self.order_number} =====\n"
            f"{product_details}\n"
            f"-------------------------\n"
            f"Subtotal: ₹{self.subtotal():.2f}\n"
            f"Final Amount: ₹{self.final_amount():.2f}"
        )


# Program

try:
    inventory = [
        Item("Gaming Laptop", 55000),
        Item("Wireless Mouse", 1500),
        Item("Mechanical Keyboard", 3000)
    ]

    offer = FlatPercentageOff(15)

    customer_order = ShoppingOrder("ORD-501", offer)

    for product in inventory:
        customer_order.add(product)

    print(customer_order)

    print(f"\nTotal items: {len(customer_order)}")

    print(f"Second item: {customer_order[1]}")

except (ValueError, TypeError) as error:
    print("Error:", error)