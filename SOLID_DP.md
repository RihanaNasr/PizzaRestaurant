"SOLID Principles and Design Patterns in the Pizza Restaurant System"


1. Singleton Pattern


SOLID Principles Addressed:
- Single Responsibility Principle (SRP):
The `InventoryManager` class is centralized in Singleton, ensuring that only one instance is used for inventory management.

- Dependency Inversion Principle (DIP):
The `InventoryManager` class is utilized by the system for managing inventory, ensuring consistency across the application as it is a Singleton.

How It Implements the Principle:
The system maintains a single inventory source by ensuring only one instance of `InventoryManager`, preventing discrepancies and ensuring consistency.


2. Factory Pattern


SOLID Principles Addressed:
- Open/Closed Principle (OCP):
The `PizzaFactory` class enables the creation of new pizza types without altering existing code, allowing for extension and modification without altering existing creation logic.

- Liskov Substitution Principle (LSP):
The `PizzaFactory` allows for the replacement of the base `Pizza` class with derived classes like `Margherita` or `Pepperoni` without altering system behavior.

How It Implements the Principle:
The Factory Pattern simplifies pizza creation, allowing future additions of new types while maintaining scalability and adhering to the OCP's interface and behavior.


3. Strategy Pattern
 

SOLID Principles Addressed:
- Open/Closed Principle (OCP):
The Strategy Pattern enables the addition of new payment methods like PayPal and Credit Card without altering the existing payment processing code.

- Dependency Inversion Principle (DIP):
The system utilizes an abstraction called `PaymentMethod` instead of concrete payment methods like `PayPal` or `CreditCard`, enhancing flexibility and ease of system extension.
 
How It Implements the Principle:
The Strategy Pattern allows for the addition of new payment methods without altering the core payment logic, ensuring flexibility and extendability in the system.


4. Decorator Pattern


SOLID Principles Addressed:
- Single Responsibility Principle (SRP):
The `ToppingDecorator` class adds functionality to pizza objects, with each topping (e.g., Cheese, Olives, Mushrooms) acting as a separate decorator, adding specific responsibility to the pizza description and cost.

- Open/Closed Principle (OCP):
The `ToppingDecorator` class allows for extension of new toppings without modifying existing classes, while the pizza object remains closed for modification and new toppings are added via decorators.

How It Implements the Principle:
The Decorator Pattern dynamically adds new toppings to the base pizza class, maintaining its responsibility while allowing for additional functionality without affecting existing code.


5. Conclusion


SOLID Principles in Action:
The Pizza Restaurant system uses SOLID principles for maintainability, extensibility, and scalability, ensuring flexibility and adaptability. The Factory, Strategy, Singleton, and Decorator patterns work together to ensure the codebase remains adaptable to new requirements.
