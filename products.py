class Product():

    #Constructor function: encapsulating instance variables into Product class
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty or None")
        self.name: str = name

        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price: float = price

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        self.quantity: int = quantity

        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        # validating that quantity is not negative
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        # validating that quantity is Integer
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")

        # checking if the new value reaches 0, if yes deactivating the product
        if quantity == 0:
            self.active = False

        # setting the instance var to the new value
        self.quantity = quantity

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:

        # checking that there is at lease 1 item to buy
        if quantity < 1:
            raise ValueError("please select at least one or more items first!")
        # checking that there is a sufficient amount of items in the store
        if quantity > self.quantity:
            raise ValueError(f"there are only {self.quantity} items left, please order a smaller or equal amount")
        # updating the instance quantity var to the new one after the purchase

        if self.quantity == quantity:
            self.active = False

        self.quantity = self.quantity - quantity
        # returning the total purchase amount
        return self.price * quantity