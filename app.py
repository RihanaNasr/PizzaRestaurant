from abc import ABC, abstractmethod

# Inventory Manager
class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

# Base Pizza Class (Abstract)
class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

# Concrete Pizza Classes
class Margherita(Pizza):
    def get_description(self):
        return "Margherita Pizza"

    def get_cost(self):
        return 150.0


class Pepperoni(Pizza):
    def get_description(self):
        return "Pepperoni Pizza"

    def get_cost(self):
        return 180.0

# Topping Decorator Class (Abstract)
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

# Concrete Topping Classes
class Cheese(ToppingDecorator):
    def get_description(self):
        return self._pizza.get_description() + " + Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + 20.0


class Olives(ToppingDecorator):
    def get_description(self):
        return self._pizza.get_description() + " + Olives"

    def get_cost(self):
        return self._pizza.get_cost() + 10.0


class Mushrooms(ToppingDecorator):
    def get_description(self):
        return self._pizza.get_description() + " + Mushrooms"

    def get_cost(self):
        return self._pizza.get_cost() + 20.0


# Payment Method Strategy Interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."


class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."


# Pizza Factory Method
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "1":
            return Margherita()
        elif pizza_type == "2":
            return Pepperoni()
        else:
            return None

# Payment Processor Class
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount):
        return self.payment_method.pay(amount)


# Main Function
def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        # Base pizza selection
        print("\nChoose your base pizza:")
        print("1. Margherita")
        print("2. Pepperoni ")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        # Create pizza using Factory
        pizza = PizzaFactory.create_pizza(pizza_choice)
        if not pizza:
            print("Invalid pizza choice!")
            continue

        # Add toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ")
            print("2. Olives ")
            print("3. Mushrooms ")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                pizza = Cheese(pizza)
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                pizza = Olives(pizza)
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        # Display final pizza details
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Show remaining inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())

        # Payment
        print("\nChoose a payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == "1":
            payment_method = PayPal()
        elif payment_choice == "2":
            payment_method = CreditCard()
        else:
            print("Invalid payment method!")
            continue

        # Process Payment
        payment_processor = PaymentProcessor(payment_method)
        payment_message = payment_processor.process_payment(pizza.get_cost())

        # Print the final message and exit the loop
        print(payment_message)
        print("\nThank you for your order!")
        break
      

if __name__ == "__main__":
    main()
